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
(`apt install pngquant` or `brew install pngquant`). With Nix, `nix develop` gives
a shell with Python 3.14, uv and pngquant, and `nix build` puts the site in `result/`
(privacy plugin off: the build sandbox has no network to localize fonts and scripts).

Pushes to `main` deploy to GitHub Pages via `.github/workflows/docs.yml`.

## Layout

| Path | What |
| --- | --- |
| `docs/` | Page sources. The folder structure mirrors the old `/wiki/<slug>` URLs. |
| `docs/assets/uploads/` | Images and PDF forms vendored from the CMS. |
| `includes/abbreviations.md` | Glossary appended to every page; terms get hover tooltips. |
| `zensical.toml` | Navigation, theme, plugins (tags, glightbox, redirects, llms.txt, minify, optimize, privacy). |
| `overrides/partials/` | computerome.dk header (menus, sign-in) and footer. |
| `src/computerome_zensical/` | Importer and weekly sync from the Strapi API. |
| `upstream/` | Converted CMS snapshots; merge base for the sync, never edit by hand. |

## Syncing from the CMS

`docs/` is the source of truth and is hand-edited. `upstream/` holds the last
machine-converted copy of each CMS page and serves as the merge base:

```bash
uv run computerome-zensical
```

For each page it prints one status line:

| Status | Meaning |
| --- | --- |
| `new` | Not in `docs/` yet (or deleted to force a re-import); written as converted. |
| `merged` | Upstream changed; `git merge-file` applied the change on top of the hand edits. |
| `conflict` | Upstream changed text that was also edited locally; diff3 markers left in the page. |
| `removed` | Gone upstream; its snapshot is dropped, the `docs/` page is kept. |
| `baseline` | Page existed without a snapshot; snapshot recorded, `docs/` untouched. |

HTTP calls retry with backoff via [stamina](https://stamina.hynek.me), honouring
`Retry-After` on 429s.

`.github/workflows/sync.yml` runs this every Monday and opens a PR on the
`upstream-sync` branch. For `new` and `conflict` pages it first runs
[Claude Code](https://github.com/anthropics/claude-code-action) to resolve markers
and restyle new pages to match the site. Setup:

1. `claude setup-token`, then store the token as the repo secret `CLAUDE_CODE_OAUTH_TOKEN`.
   Without it the PR still opens, with conflict markers left for a human (as a draft).
2. Settings → Actions → General → enable *Allow GitHub Actions to create and approve pull requests*.

PRs opened with `GITHUB_TOKEN` do not trigger other workflows, so the sync job runs the
strict build itself and opens the PR as a draft if it fails.

It pulls `https://delphiapp.computerome.dk/strapi/api/wikis`, converts the CMS
HTML/CommonMark mix to Python-Markdown (admonitions, list indentation, icons,
escaped placeholders), rewrites wiki links to relative `.md` links and vendors
uploads up to 5 MB. Videos (about 3 GB) and the large workshop slide decks stay
linked to the CMS.

The old all-in-one `user-guide` page duplicated the split pages, so it is not
imported; `/user-guide/` redirects to Getting Started.

Converter checks: `uv run python tests/test_convert.py`.
