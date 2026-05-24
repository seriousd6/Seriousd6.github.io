#!/usr/bin/env bash
# fetch-bible-data.sh
# Downloads public-domain Bible JSON from api.getbible.net and transforms
# it into the project schema at data/bible/{VERSION}/{bookId}.json
#
# Usage (from repo root):
#   bash scripts/fetch-bible-data.sh             # all versions
#   bash scripts/fetch-bible-data.sh KJV         # one version only
#   bash scripts/fetch-bible-data.sh KJV WEB     # two versions
#
# NOTE: BSB (Berean Standard Bible) is CC0 and sourced separately via
#   scripts/fetch-bsb.py (uses scrollmapper/bible_databases on GitHub).
#   BSB is NOT available on getbible.net.
#
# Requires: curl, python3
# Run once locally; commit the resulting data/bible/ files to the repo.
# The script is idempotent — it skips files that already exist.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA_DIR="$REPO_ROOT/data/bible"
BOOKS_JSON="$DATA_DIR/books.json"

# Map project version IDs to getbible.net translation slugs
declare -A VERSION_SLUGS=(
  [KJV]="kjv"
  [ASV]="asv"
  [WEB]="web"
)

# Determine which versions to fetch
if [ $# -eq 0 ]; then
  VERSIONS=("KJV" "ASV" "WEB")
else
  VERSIONS=("$@")
fi

# Extract bookNumber→id mapping from books.json using python
BOOK_MAP=$(python3 - "$BOOKS_JSON" <<'PYEOF'
import json, sys
books = json.load(open(sys.argv[1]))
for b in books:
    print(f"{b['bookNumber']}:{b['id']}:{b['name']}")
PYEOF
)

TRANSFORM_SCRIPT=$(cat <<'PYEOF'
import json, sys

version_id  = sys.argv[1]
book_id     = sys.argv[2]
book_name   = sys.argv[3]
input_file  = sys.argv[4]
output_file = sys.argv[5]

with open(input_file) as f:
    raw = json.load(f)

# api.getbible.net v2 format (current):
# {
#   "nr": 43, "name": "John",
#   "chapters": [
#     { "chapter": 1, "name": "John 1",
#       "verses": [ {"chapter":1,"verse":1,"name":"John 1:1","text":"..."}, ... ] },
#     ...
#   ]
# }
#
# Older cdn format had chapters as a dict with string keys and verses as a
# dict of {verse_num: {verse:N, text:"..."}}. Both formats are handled below.

chapters_raw = raw.get("chapters", [])
chapters_out = {}

if isinstance(chapters_raw, list):
    for ch_obj in chapters_raw:
        ch_key = str(ch_obj.get("chapter", ""))
        if not ch_key:
            continue
        verses_raw = ch_obj.get("verses", [])
        verses_out = {}
        if isinstance(verses_raw, list):
            for v_obj in verses_raw:
                v_key = str(v_obj.get("verse", ""))
                text  = v_obj.get("text", "").strip()
                if v_key and text:
                    verses_out[v_key] = text
        elif isinstance(verses_raw, dict):
            for v_key, v_data in verses_raw.items():
                text = v_data.get("text", "").strip() if isinstance(v_data, dict) else str(v_data).strip()
                if text:
                    verses_out[str(v_key)] = text
        if verses_out:
            chapters_out[ch_key] = verses_out
elif isinstance(chapters_raw, dict):
    for ch_key, ch_data in chapters_raw.items():
        verses_raw = ch_data.get("verses", {}) if isinstance(ch_data, dict) else {}
        verses_out = {}
        for v_key, v_data in verses_raw.items():
            text = v_data.get("text", "").strip() if isinstance(v_data, dict) else str(v_data).strip()
            if text:
                verses_out[str(v_key)] = text
        if verses_out:
            chapters_out[str(ch_key)] = verses_out

out = {
    "version": version_id,
    "book": book_name,
    "bookId": book_id,
    "chapters": chapters_out
}

with open(output_file, "w") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))

print(f"  Wrote {len(chapters_out)} chapters, {sum(len(v) for v in chapters_out.values())} verses")
PYEOF
)

echo "Bible data fetcher — starting"
echo "Output directory: $DATA_DIR"
echo ""

TOTAL_OK=0
TOTAL_SKIP=0
TOTAL_FAIL=0

for VERSION in "${VERSIONS[@]}"; do
  SLUG="${VERSION_SLUGS[$VERSION]:-}"
  if [ -z "$SLUG" ]; then
    echo "ERROR: Unknown version '$VERSION'. Known versions: ${!VERSION_SLUGS[*]}"
    continue
  fi

  VERSION_DIR="$DATA_DIR/$VERSION"
  mkdir -p "$VERSION_DIR"
  echo "── $VERSION (slug: $SLUG) ──────────────────────────────"

  while IFS=: read -r BOOK_NUM BOOK_ID BOOK_NAME; do
    OUT_FILE="$VERSION_DIR/${BOOK_ID}.json"

    if [ -f "$OUT_FILE" ]; then
      echo "  [$BOOK_NUM] $BOOK_NAME — skipped (exists)"
      TOTAL_SKIP=$((TOTAL_SKIP + 1))
      continue
    fi

    URL="https://api.getbible.net/v2/${SLUG}/${BOOK_NUM}.json"
    TMP_FILE=$(mktemp /tmp/bsw_bible_XXXXXX.json)

    if curl -sSf --max-time 30 -o "$TMP_FILE" "$URL" 2>/dev/null; then
      if python3 -c "$TRANSFORM_SCRIPT" "$VERSION" "$BOOK_ID" "$BOOK_NAME" "$TMP_FILE" "$OUT_FILE" 2>&1; then
        echo "  [$BOOK_NUM] $BOOK_NAME — OK → $BOOK_ID.json"
        TOTAL_OK=$((TOTAL_OK + 1))
      else
        echo "  [$BOOK_NUM] $BOOK_NAME — TRANSFORM ERROR"
        TOTAL_FAIL=$((TOTAL_FAIL + 1))
      fi
    else
      echo "  [$BOOK_NUM] $BOOK_NAME — DOWNLOAD FAILED ($URL)"
      TOTAL_FAIL=$((TOTAL_FAIL + 1))
    fi

    rm -f "$TMP_FILE"
    # Be polite to the CDN
    sleep 0.25

  done <<< "$BOOK_MAP"

  echo ""
done

echo "────────────────────────────────────────────────"
echo "Done. OK: $TOTAL_OK  Skipped: $TOTAL_SKIP  Failed: $TOTAL_FAIL"

if [ $TOTAL_FAIL -gt 0 ]; then
  echo ""
  echo "Re-run to retry failed downloads (script skips existing files)."
fi
