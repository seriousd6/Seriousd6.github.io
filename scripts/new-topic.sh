#!/usr/bin/env bash
# Usage: bash scripts/new-topic.sh <slug> "Title" "Short description"
#
# Creates topics/<slug>/index.html from the _template and opens it.

set -e
SLUG="${1:-}"
TITLE="${2:-$SLUG}"
DESC="${3:-A Bible study on $TITLE.}"

if [ -z "$SLUG" ]; then
  echo "Usage: bash scripts/new-topic.sh <slug> \"Title\" \"Description\""
  exit 1
fi

DEST="topics/$SLUG"
if [ -d "$DEST" ]; then
  echo "❌  $DEST already exists."
  exit 1
fi

cp -r topics/_template "$DEST"
sed -i "s/TOPIC_TITLE/$TITLE/g"       "$DEST/index.html"
sed -i "s/TOPIC_DESCRIPTION/$DESC/g"  "$DEST/index.html"

echo "✅  Created $DEST/index.html"
echo "   → Add a card in topics/index.html and index.html"
