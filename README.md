# Computerome Wiki (Zensical)

The [Computerome wiki](https://computerome.dk/wiki) ported from its Strapi CMS to a
static [Zensical](https://zensical.org) site.

Live site: <https://jgalabs.dk/computerome-zensical/>

## Usage

```bash
uv sync
uv run zensical serve      # live preview on http://localhost:8000
uv run zensical build      # static site in site/
```

Builds need [`pngquant`](https://pngquant.org) on `PATH` for the image optimizer
(`apt install pngquant`, `brew install pngquant` or `nix shell nixpkgs#pngquant`).

Pushes to `main` deploy to GitHub Pages via `.github/workflows/docs.yml`.

## Layout

| Path | What |
| --- | --- |
| `docs/` | Page sources. The folder structure mirrors the old `/wiki/<slug>` URLs. |
| `docs/assets/uploads/` | Images and PDF forms vendored from the CMS. |
| `includes/abbreviations.md` | Glossary appended to every page; terms get hover tooltips. |
| `zensical.toml` | Navigation, theme, plugins (tags, glightbox, redirects, llms.txt, minify, optimize, privacy). |
| `overrides/partials/` | computerome.dk header (menus, sign-in) and footer. |
| `src/computerome_zensical/` | One-shot importer from the Strapi API. |

## Re-importing from the CMS

`docs/` is the source of truth now. The importer only writes pages that do not
exist yet, so hand edits are never overwritten. To re-import a page, delete it
and run:

```bash
uv run computerome-zensical
```

It pulls `https://delphiapp.computerome.dk/strapi/api/wikis`, converts the CMS
HTML/CommonMark mix to Python-Markdown (admonitions, list indentation, icons,
escaped placeholders), rewrites wiki links to relative `.md` links and vendors
uploads up to 5 MB. Videos (about 3 GB) and the large workshop slide decks stay
linked to the CMS.

The old all-in-one `user-guide` page duplicated the split pages, so it is not
imported; `/user-guide/` redirects to Getting Started.

Converter checks: `uv run python tests/test_convert.py`.
