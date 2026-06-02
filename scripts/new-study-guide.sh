#!/usr/bin/env bash
# Usage: bash scripts/new-study-guide.sh <slug> "Guide Title"
# Creates study-guides/<slug>/index.html from the _template and prints the
# data/topics.json entry to add manually.

set -euo pipefail

SLUG="${1:-}"
TITLE="${2:-}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$SCRIPT_DIR")"

if [[ -z "$SLUG" || -z "$TITLE" ]]; then
  echo "Usage: bash scripts/new-study-guide.sh <slug> \"Guide Title\""
  exit 1
fi

DEST="$ROOT/study-guides/$SLUG"
TEMPLATE="$ROOT/study-guides/_template/index.html"

if [[ -d "$DEST" ]]; then
  echo "Error: $DEST already exists"
  exit 1
fi

mkdir -p "$DEST"
sed \
  -e "s/GUIDE_TITLE/$TITLE/g" \
  -e "s/GUIDE_DESCRIPTION/A study guide on $TITLE./g" \
  "$TEMPLATE" > "$DEST/index.html"

echo "Created: $DEST/index.html"
echo ""
echo "Add this entry to data/topics.json:"
echo "  {"
echo "    \"slug\": \"$SLUG\","
echo "    \"label\": \"$TITLE\","
echo "    \"type\": \"study\","
echo "    \"href\": \"study-guides/$SLUG/\""
echo "  },"
echo ""
echo "Then add a card to study-guides/index.html."
