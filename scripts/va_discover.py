#!/usr/bin/env python3
"""
va_discover.py — Verse Auditor discovery script.

Scans section directory patterns, syncs VA_PROGRESS.md:
  - Adds new files as `not_started` rows
  - Marks rows for missing files as `removed` (never deletes rows)
  - Updates Last discovery / Next discovery due timestamps in the header

Run from repo root: python3 scripts/va_discover.py
"""

import re
import sys
import glob
import pathlib
from datetime import datetime, timezone, timedelta

ROOT = pathlib.Path('.')
PROGRESS_FILE = ROOT / 'working' / 'VA_PROGRESS.md'

# ---------------------------------------------------------------------------
# Section definitions — mirrors va_process.py's understanding
# ---------------------------------------------------------------------------

SECTIONS = {
    'T': {
        'label': 'Traditional Commentaries',
        'globs': [
            'data/commentary/ellicott/*.json',
            'data/commentary/jfb/*.json',
            'data/commentary/barnes/*.json',
            'data/commentary/clarke/*.json',
            'data/commentary/wesley/*.json',
            'data/commentary/rwp/*.json',
            'data/commentary/calvin/*.json',
            'data/commentary/synthesis/*.json',
        ],
        'rules': 'R1,R2,R3,R4,R5,R6',
        'file_type': 'json_commentary',
    },
    'M': {
        'label': 'MKT Commentaries',
        # Per-chapter dirs: data/commentary/mkt-original/{book}/{ch}.json
        'globs': [
            'data/commentary/mkt-original/*/',
            'data/commentary/mkt-context/*/',
            'data/commentary/mkt-christ/*/',
        ],
        'rules': 'R1,R2,R3,R5,R6',
        'file_type': 'json_commentary_chapter_dir',
    },
    'E': {
        'label': 'Echoes',
        'globs': ['data/echoes/*.json'],
        'rules': 'R1,R2',
        'file_type': 'json_echoes',
    },
    'L': {
        'label': 'Library HTML',
        'globs': ['data/library/html/*.html'],
        'rules': 'R1,R2,R3',
        'file_type': 'html',
    },
    'D': {
        'label': 'Library Docs JSON',
        'globs': ['data/library/docs/*.json'],
        'rules': 'R1,R2,R3',
        'file_type': 'json_library_doc',
    },
    'K': {
        'label': 'Book Study JSON',
        'globs': ['data/workshop/book-study/*.json'],
        'rules': 'R1,R2',
        'file_type': 'json_book_study',
    },
    'P': {
        'label': 'Topic Pages',
        'globs': ['topics/**/*.html'],
        'rules': 'R1,R2,R3,R5,R6,R7',
        'file_type': 'html',
    },
    'O': {
        'label': 'Other HTML',
        'globs': [
            'verse-study/index.html',
            'dictionary/index.html',
            'studies/index.html',
            'bookmarks/index.html',
            'compare/index.html',
            'index.html',
        ],
        'rules': 'R1,R2',
        'file_type': 'html',
    },
}

SECTION_ORDER = ['T', 'M', 'E', 'L', 'D', 'K', 'P', 'O']


# ---------------------------------------------------------------------------
# VA_PROGRESS.md parsing and serialization
# ---------------------------------------------------------------------------

def now_iso():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def parse_progress(text):
    """Parse VA_PROGRESS.md into:
      header_lines: list of raw header lines (before first ## Section)
      sections: dict of section_code -> {'raw_header': str, 'rows': [{'file': str, 'status': str, 'refs': str, 'run': str, 'notes': str}]}
    """
    lines = text.splitlines()
    header_lines = []
    sections = {}
    current_section = None
    in_table = False
    table_header_seen = False

    for line in lines:
        m_sec = re.match(r'^## Section ([A-Z]) —', line)
        if m_sec:
            code = m_sec.group(1)
            current_section = code
            sections[code] = {'raw_header': line, 'globs_comment': '', 'rows': [], 'after_header': []}
            in_table = False
            table_header_seen = False
            continue

        if current_section is None:
            header_lines.append(line)
            continue

        sec = sections[current_section]

        # Capture the globs comment line
        if line.startswith('<!-- globs:'):
            sec['globs_comment'] = line
            continue

        # Table separator / header
        if re.match(r'^\| File', line):
            in_table = True
            table_header_seen = True
            continue
        if re.match(r'^\|[-|]+\|', line) and table_header_seen:
            continue

        if in_table and line.startswith('|'):
            cols = [c.strip() for c in line.strip('|').split('|')]
            if len(cols) >= 5:
                sec['rows'].append({
                    'file': cols[0],
                    'status': cols[1],
                    'refs': cols[2],
                    'run': cols[3],
                    'notes': cols[4],
                })
            continue

        # Blank lines or non-table lines within a section
        if not line.startswith('|'):
            in_table = False
            table_header_seen = False
            sec['after_header'].append(line)

    return header_lines, sections


def scan_section_files(section_code):
    """Glob all files/dirs for a section, returning sorted list of relative path strings.
    Patterns ending in '/' match directories only; others match files only."""
    sec = SECTIONS[section_code]
    found = []
    for pattern in sec['globs']:
        dir_pattern = pattern.endswith('/')
        for f in sorted(glob.glob(str(ROOT / pattern), recursive=True)):
            p = pathlib.Path(f)
            if dir_pattern and p.is_dir():
                found.append(str(p.relative_to(ROOT)))
            elif not dir_pattern and p.is_file():
                found.append(str(p.relative_to(ROOT)))
    return sorted(set(found))


def sync_section(sec_data, on_disk_files):
    """Diff current rows vs. on-disk files; return updated rows list plus counts."""
    existing = {row['file']: row for row in sec_data['rows']}
    new_count = 0
    removed_count = 0

    updated_rows = []

    # Mark removed
    for f, row in existing.items():
        if f not in on_disk_files and row['status'] != 'removed':
            row = dict(row)
            row['status'] = 'removed'
            removed_count += 1
        updated_rows.append(row)

    # Add new
    existing_files = set(row['file'] for row in sec_data['rows'])
    for f in on_disk_files:
        if f not in existing_files:
            updated_rows.append({
                'file': f,
                'status': 'not_started',
                'refs': '—',
                'run': '—',
                'notes': '—',
            })
            new_count += 1

    # Sort: active rows first, removed last; within each group sort by file path
    active = [r for r in updated_rows if r['status'] != 'removed']
    removed = [r for r in updated_rows if r['status'] == 'removed']
    active.sort(key=lambda r: r['file'])
    removed.sort(key=lambda r: r['file'])
    return active + removed, new_count, removed_count


def build_progress_md(header_lines, sections):
    """Serialize sections dict back to VA_PROGRESS.md text."""
    parts = ['\n'.join(header_lines)]

    for code in SECTION_ORDER:
        if code not in sections:
            sec_def = SECTIONS[code]
            # Create empty section from scratch
            parts.append(f'\n## Section {code} — {sec_def["label"]}')
            globs_str = ' '.join(sec_def['globs'])
            parts.append(f'<!-- globs: {globs_str} -->')
            parts.append('')
            parts.append('| File | Status | Refs Fixed | Last Run | Notes |')
            parts.append('|---|---|---|---|---|')
        else:
            sec = sections[code]
            parts.append(f'\n{sec["raw_header"]}')
            # Always regenerate globs comment from current SECTIONS definition
            globs_str = ' '.join(SECTIONS[code]['globs'])
            parts.append(f'<!-- globs: {globs_str} -->')
            parts.append('')
            parts.append('| File | Status | Refs Fixed | Last Run | Notes |')
            parts.append('|---|---|---|---|---|')
            for row in sec['rows']:
                parts.append(
                    f'| {row["file"]} | {row["status"]} | {row["refs"]} | {row["run"]} | {row["notes"]} |'
                )

    return '\n'.join(parts) + '\n'


def update_header_timestamps(header_lines, loop_restarts_unchanged=True):
    """Update Last discovery and Next discovery due lines in the header."""
    now = now_iso()
    next_due = (datetime.now(timezone.utc) + timedelta(hours=24)).strftime('%Y-%m-%dT%H:%M:%SZ')
    updated = []
    for line in header_lines:
        if line.startswith('Last discovery:'):
            updated.append(f'Last discovery: {now}')
        elif line.startswith('Next discovery due:'):
            updated.append(f'Next discovery due: {next_due}')
        else:
            updated.append(line)
    return updated


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not PROGRESS_FILE.exists():
        print(f'ERROR: {PROGRESS_FILE} not found. Create it first (header + empty section headers).', file=sys.stderr)
        sys.exit(1)

    text = PROGRESS_FILE.read_text(encoding='utf-8')
    header_lines, sections = parse_progress(text)

    total_new = 0
    total_removed = 0

    for code in SECTION_ORDER:
        on_disk = scan_section_files(code)

        if code not in sections:
            sec_def = SECTIONS[code]
            sections[code] = {
                'raw_header': f'## Section {code} — {sec_def["label"]}',
                'globs_comment': '<!-- globs: ' + ' '.join(sec_def['globs']) + ' -->',
                'rows': [],
                'after_header': [],
            }

        updated_rows, new_count, removed_count = sync_section(sections[code], on_disk)
        sections[code]['rows'] = updated_rows
        total_new += new_count
        total_removed += removed_count
        print(f'  Section {code}: {len(on_disk)} on disk, +{new_count} new, -{removed_count} removed')

    header_lines = update_header_timestamps(header_lines)
    new_text = build_progress_md(header_lines, sections)
    PROGRESS_FILE.write_text(new_text, encoding='utf-8')

    print(f'\nDone. Added {total_new} new rows, marked {total_removed} as removed.')
    print(f'VA_PROGRESS.md updated.')


if __name__ == '__main__':
    main()
