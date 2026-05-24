# Bible Study Website

A personal Bible study reference site hosted on GitHub Pages.

## Features (planned / in progress)

- 📖 Multiple Bible versions (KJV, NIV, ESV, NASB …)
- 🔗 Hotlinked Bible references throughout all content
- 📚 Topical study pages (Prayer, Revelation, …)
- 🔍 Cross-reference lookup
- 📱 Mobile-friendly layout

## Live Site

> https://<your-github-username>.github.io/bible-study/

## Project Structure

```
bible-study/
├── index.html              # Home / landing page
├── assets/
│   ├── css/style.css       # Global styles
│   ├── js/main.js          # Core JS (reference linking, etc.)
│   └── images/
├── data/
│   ├── versions/           # Metadata for each Bible version
│   ├── books/              # Book/chapter/verse structure (JSON)
│   └── references/         # Pre-built cross-reference maps
├── topics/
│   ├── index.html          # Topics listing page
│   ├── prayer/index.html
│   ├── revelation/index.html
│   └── _template/          # Copy this to start a new topic
├── _includes/              # Shared HTML partials (header, footer, …)
├── _layouts/               # Base page layouts
└── scripts/                # Build / utility scripts
```

## Adding a New Topic

1. Copy `topics/_template/` to `topics/<your-topic>/`
2. Edit `topics/<your-topic>/index.html`
3. Add a card in `topics/index.html`
4. Use `<a class="ref" data-ref="John 3:16">John 3:16</a>` for hotlinked references

## Bible Reference Linking

Any element with `class="ref"` and a `data-ref` attribute is auto-linked by
`assets/js/main.js` to the configured Bible API (Bible Gateway by default).

```html
<a class="ref" data-ref="Romans 8:28">Romans 8:28</a>
```

## GitHub Pages Setup

1. Push to GitHub
2. Go to **Settings → Pages**
3. Source: `main` branch, `/ (root)` folder
4. Your site is live at `https://<username>.github.io/<repo>/`

## Development

Open any `.html` file directly in a browser for local preview — no build step
required. For live-reload during editing, run:

```bash
# Python 3 (built-in)
python3 -m http.server 8080
```

Then visit `http://localhost:8080`.

## Claude Agent Notes

See `CLAUDE.md` for project context and conventions used when working with
Claude Code or Claude AI assistance.
