# data/versions/

`versions.json` lists every Bible version the site supports.

The user's selected version is saved in `localStorage` under `bsw_version`.
The version picker in the header reads this file to build its `<select>` options
(or they can be hard-coded in `_includes/header.html`).
