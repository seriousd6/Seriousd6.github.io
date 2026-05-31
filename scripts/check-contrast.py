#!/usr/bin/env python3
"""
check-contrast.py — WCAG AA contrast ratio checker for style.css.

Checks every meaningful text-on-background color pair in both light and dark mode.
Fails pairs that fall below 4.5:1 (normal text) or 3:1 (large/UI text).

Run from repo root:
    python3 scripts/check-contrast.py

WCAG AA thresholds:
    Normal text  (<18pt / <14pt bold): 4.5:1
    Large text   (≥18pt / ≥14pt bold): 3:1
    UI components / graphical objects: 3:1
"""

import re
import sys
import math


# ── Color parsing ─────────────────────────────────────────────────────────────

def hex_to_rgb(h):
    """Convert #rrggbb or #rgb hex string to (r, g, b) in 0–255 range."""
    h = h.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def srgb_to_linear(c):
    """Convert 0–255 sRGB channel to linear light value per WCAG formula."""
    s = c / 255.0
    if s <= 0.04045:
        return s / 12.92
    return ((s + 0.055) / 1.055) ** 2.4


def relative_luminance(hex_color):
    """Compute WCAG relative luminance for a hex color."""
    r, g, b = hex_to_rgb(hex_color)
    lr = srgb_to_linear(r)
    lg = srgb_to_linear(g)
    lb = srgb_to_linear(b)
    return 0.2126 * lr + 0.7152 * lg + 0.0722 * lb


def contrast_ratio(fg, bg):
    """Compute WCAG contrast ratio between two hex colors."""
    l1 = relative_luminance(fg)
    l2 = relative_luminance(bg)
    lighter = max(l1, l2)
    darker  = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


# ── Color pairs to check ──────────────────────────────────────────────────────
# Each entry: (label, fg_hex, bg_hex, threshold)
# threshold: 4.5 for normal text, 3.0 for large text or UI components

LIGHT_MODE = [
    # --color-on-primary: text placed on background: var(--color-primary) buttons/badges
    ("Light / on-primary text on primary bg", "#ffffff", "#5c3d1e", 4.5),
    # Main content text on page backgrounds
    ("Light / body text on page bg",          "#2c2416", "#faf8f4", 4.5),
    ("Light / body text on surface",          "#2c2416", "#ffffff", 4.5),
    ("Light / muted text on page bg",         "#7a6a55", "#faf8f4", 4.5),
    ("Light / muted text on surface",         "#7a6a55", "#ffffff", 4.5),
    ("Light / primary (link) on page bg",     "#5c3d1e", "#faf8f4", 4.5),
    ("Light / primary (link) on surface",     "#5c3d1e", "#ffffff", 4.5),
    # --color-accent: used for <a> links and .ref scripture links (text, not decorative)
    ("Light / accent (links) on page bg",     "#8c6a00", "#faf8f4", 4.5),
    ("Light / accent (links) on surface",     "#8c6a00", "#ffffff", 4.5),

    # Sidebar — always renders dark even in light mode
    ("Light sidebar / nav text on sb-bg",     "#e8d9bb", "#32200e", 4.5),
    ("Light sidebar / muted on sb-bg",        "#a08a68", "#32200e", 4.5),   # --sb-muted fixed
    ("Light sidebar / active text on sb-bg",  "#e8c87a", "#32200e", 4.5),
    # Hardcoded sidebar child link colors
    ("Light sidebar / sb-child on sb-bg",     "#c4b490", "#32200e", 4.5),
    ("Light sidebar / sb-subchild on sb-bg",  "#9e8f6e", "#32200e", 4.5),
    ("Light sidebar / sb-sublabel on sb-bg",  "#9a7a50", "#32200e", 3.0),   # UI label — 3:1 threshold; color fixed
    ("Light sidebar / sb-subgroup-btn",       "#b8a880", "#32200e", 4.5),
    ("Light sidebar / logo on sb-bg",         "#f0e6d0", "#32200e", 4.5),
]

DARK_MODE = [
    # --color-on-primary: dark text on golden primary bg (was white — failed at ~1.5:1)
    ("Dark / on-primary text on primary bg",  "#1a1208", "#e8c87a", 4.5),
    # Main content
    ("Dark / body text on page bg",           "#e8dfc8", "#1a1208", 4.5),
    ("Dark / body text on surface",           "#e8dfc8", "#231a0d", 4.5),
    ("Dark / muted text on page bg",          "#9a8870", "#1a1208", 4.5),
    ("Dark / muted text on surface",          "#9a8870", "#231a0d", 4.5),
    ("Dark / primary (golden) on page bg",    "#e8c87a", "#1a1208", 4.5),
    ("Dark / primary on surface",             "#e8c87a", "#231a0d", 4.5),
    ("Dark / accent on page bg",              "#d4a017", "#1a1208", 4.5),
    ("Dark / accent on surface",              "#d4a017", "#231a0d", 4.5),
    # Dark mode button surfaces
    ("Dark / btn text on btn-bg",             "#e8c87a", "#3a2d18", 4.5),

    # Sidebar (darker in dark mode)
    ("Dark sidebar / nav text on sb-bg",      "#e8d9bb", "#120d05", 4.5),
    ("Dark sidebar / muted on sb-bg",         "#9e8a6e", "#120d05", 4.5),   # --sb-muted fixed
    ("Dark sidebar / active text on sb-bg",   "#e8c87a", "#120d05", 4.5),
    ("Dark sidebar / logo on sb-bg",          "#f0e6d0", "#120d05", 4.5),
    # Hardcoded child colors unchanged in dark mode (sidebar is always dark)
    ("Dark sidebar / sb-child on sb-bg",      "#c4b490", "#120d05", 4.5),
    ("Dark sidebar / sb-subchild on sb-bg",   "#9e8f6e", "#120d05", 4.5),
    ("Dark sidebar / sb-sublabel on sb-bg",   "#9a7a50", "#120d05", 3.0),   # UI label — 3:1 threshold; color fixed
    ("Dark sidebar / sb-subgroup-btn",        "#b8a880", "#120d05", 4.5),
]


# ── Runner ────────────────────────────────────────────────────────────────────

def check_all(pairs, mode_label):
    failures = []
    print(f"\n{'═' * 60}")
    print(f"  {mode_label}")
    print(f"{'═' * 60}")
    for label, fg, bg, threshold in pairs:
        ratio = contrast_ratio(fg, bg)
        passed = ratio >= threshold
        status = "PASS ✓" if passed else "FAIL ✗"
        print(f"  {status}  {ratio:5.2f}:1  (need {threshold}:1)  {label}")
        print(f"         fg={fg}  bg={bg}")
        if not passed:
            failures.append((label, fg, bg, ratio, threshold))
    return failures


def main():
    all_failures = []
    all_failures += check_all(LIGHT_MODE, "LIGHT MODE")
    all_failures += check_all(DARK_MODE,  "DARK MODE")

    print(f"\n{'═' * 60}")
    if not all_failures:
        print("  All pairs pass WCAG AA. ✓")
    else:
        print(f"  {len(all_failures)} failure(s) found:")
        for label, fg, bg, ratio, threshold in all_failures:
            print(f"  • {label}")
            print(f"    {ratio:.2f}:1 vs required {threshold}:1  (fg={fg}  bg={bg})")
        sys.exit(1)
    print(f"{'═' * 60}\n")


if __name__ == "__main__":
    main()
