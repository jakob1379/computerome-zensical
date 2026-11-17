import json
import posixpath
import re
import sys
import textwrap
import urllib.request
from pathlib import Path

API = "https://delphiapp.computerome.dk/strapi/api"
UPLOADS = "https://delphiapp.computerome.dk/strapi/uploads/"
SITE = "https://computerome.dk"
DOCS = Path("docs")
ASSETS = "assets/uploads"
SKIP = {"user-guide"}
MAX_VENDORED_BYTES = 5_000_000

ICONS = {
    "check-circle": ":fontawesome-solid-circle-check:",
    "file": ":fontawesome-solid-file-pdf:",
    "video": ":fontawesome-solid-video:",
    "mobile": ":fontawesome-solid-mobile-screen:",
    "apple": ":fontawesome-brands-apple:",
    "android": ":fontawesome-brands-android:",
}

ADMONITION_KINDS = {"info": "info", "tips": "tip"}


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "computerome-zensical"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def size(url: str) -> int:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "computerome-zensical"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return int(resp.headers.get("Content-Length", 0))


def vendorable(name: str) -> bool:
    return not name.endswith(".mp4") and size(UPLOADS + name) <= MAX_VENDORED_BYTES


def slugify(text: str) -> str:
    text = re.sub(r"[`*_\[\]()]", "", text).strip().lower()
    return re.sub(r"[^\w]+", "-", text).strip("-")


def page_paths(wikis: list[dict]) -> dict[str, str]:
    parents = {w["parent"]["id"] for w in wikis if w.get("parent")}
    paths = {}
    for w in wikis:
        slug = w["url_slug_full"]
        paths[slug] = f"{slug}/index.md" if w["id"] in parents else f"{slug}.md"
    return paths


LIST_ITEM = re.compile(r"^( *)([-*+]|\d+[.)])( +)\S")
FENCE = re.compile(r"^ *(`{3,}|~{3,})")


def normalize_lists(text: str) -> str:
    """Re-indent CommonMark-style lists and add the blank lines Python-Markdown needs around blocks."""
    out: list[str] = []
    stack: list[tuple[int, int]] = []  # (content column in source, indent in output) per open list item
    fence, shift = "", 0
    for line in text.split("\n"):
        width = len(line) - len(line.lstrip(" "))
        prev = out[-1] if out else ""
        if fence:
            out.append(" " * max(0, width + shift) + line.lstrip(" ") if line.strip() else line)
            if line.strip().startswith(fence):
                fence = ""
            continue
        if not line.strip():
            out.append(line)
            continue
        if re.match(r"^#{1,6} ", prev):
            out.append("")
        item = LIST_ITEM.match(line)
        if item:
            if not stack and prev.strip() and not LIST_ITEM.match(prev):
                out.append("")
            while stack and width < stack[-1][0]:
                stack.pop()
            new = stack[-1][1] + 4 if stack else 0
            stack.append((width + len(item[2]) + len(item[3]), new))
            line = " " * new + line.lstrip(" ")
        elif stack and width == 0 and not prev.strip():
            stack.clear()
        elif stack and width > 0:
            while len(stack) > 1 and width < stack[-1][0]:
                stack.pop()
            column, new = stack[-1]
            line = " " * (new + 4 + max(0, width - column)) + line.lstrip(" ")
        if not stack and line.startswith("|") and prev.strip() and not prev.startswith("|"):
            out.append("")
        if FENCE.match(line):
            fence = FENCE.match(line)[1]
            shift = (len(line) - len(line.lstrip(" "))) - width
        out.append(line)
    return "\n".join(out)


HTML_TAGS = {"a", "abbr", "b", "br", "code", "details", "div", "em", "i", "img", "kbd", "p", "pre", "source", "span", "strong", "sub", "summary", "sup", "video"}
PLACEHOLDER = re.compile(r"(`+)(?:(?!\n\s*\n).)+?\1|<([A-Za-z_][\w .-]*)>", re.S)


def escape_placeholders(text: str) -> str:
    """Escape `<user_name>`-style placeholders outside code so they are not swallowed as HTML tags."""
    chunks, fence, buf = [], "", []
    for line in text.split("\n"):
        match = FENCE.match(line)
        if fence or match:
            if not fence:
                if buf:
                    chunks.append(("text", "\n".join(buf)))
                buf, fence = [], match[1]
            elif line.strip().startswith(fence):
                fence = ""
            chunks.append(("code", line))
            continue
        buf.append(line)
    if buf:
        chunks.append(("text", "\n".join(buf)))

    def escape(m: re.Match) -> str:
        if m[2] is None or m[2].split()[0].lower() in HTML_TAGS:
            return m[0]
        return f"&lt;{m[2]}&gt;"

    parts = [PLACEHOLDER.sub(escape, body) if kind == "text" else body for kind, body in chunks]
    return "\n".join(parts)


def indent(body: str) -> str:
    body = normalize_lists(textwrap.dedent(body)).strip("\n")
    return textwrap.indent(body, "    ", lambda line: line.strip() != "")


def admonition(kind: str, title: str, body: str) -> str:
    title = title.strip().rstrip(":").strip()
    header = f"!!! {kind}" if title.lower() == kind else f'!!! {kind} "{title}"'
    return f"\n{header}\n\n{indent(body)}\n\n"


def quote_kind(title: str) -> str:
    lowered = title.lower()
    if "important" in lowered or "warning" in lowered:
        return "warning"
    if "billing" in lowered:
        return "info"
    if "key notes" in lowered:
        return "abstract"
    return "note"


def convert_quotes(text: str) -> str:
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        match = re.match(r"^>\s*\*\*([^*]+?)\*\*:?\s*(.*)$", lines[i])
        if not match:
            out.append(lines[i])
            i += 1
            continue
        title, rest = match.groups()
        body = [rest] if rest.strip() else []
        i += 1
        while i < len(lines) and lines[i].startswith(">"):
            body.append(re.sub(r"^> ?", "", lines[i]))
            i += 1
        kind = quote_kind(title)
        title = kind if title.strip().rstrip(":").lower() == "note" else title
        out.append(admonition(kind, title, "\n".join(body)))
    return "\n".join(out)


def html_to_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(
        r"(?:<p>([^<]*?)</p>\s*)?<video[^>]*>\s*<source src=\"([^\"]+)\"[^>]*>.*?</video>",
        lambda m: (f"**{m[1].strip().rstrip(':')}**\n\n" if m[1] else "")
        + f'<video controls preload="none" width="100%"><source src="{m[2]}" type="video/mp4"></video>\n',
        text,
        flags=re.S,
    )
    text = re.sub(r"</?br\s*/?>", "\n", text)
    text = normalize_lists(text)
    text = re.sub(
        r'<div class="(\w+)">\s*<div>\s*<span class="title">(.*?)</span>(.*?)</div>\s*</div>',
        lambda m: admonition(ADMONITION_KINDS.get(m[1], "note"), m[2], m[3]),
        text,
        flags=re.S,
    )
    text = re.sub(r'<div id="[^"]*"\s*\n(#+ .*?)\n</div>', r"\1", text)
    text = re.sub(r'<span class="title">(.*?)</span>', r"**\1**", text)
    text = re.sub(
        r'<img class="([^"]*)" src="([^"]+)" alt="[^"]*">',
        lambda m: f"![Screenshot]({m[2]})"
        + ('{ width="80" }' if "w-20" in m[1] else "{ loading=lazy }"),
        text,
    )
    text = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f"[{m[2].strip()}]({m[1]})", text, flags=re.S)
    text = re.sub(r"<b>(.*?)</b>", lambda m: f"**{m[1].strip()}**", text, flags=re.S)
    text = re.sub(
        r'<i class="fa[slbr]? fa-([\w-]+)[^"]*"></i>',
        lambda m: ICONS.get(m[1], ""),
        text,
    )
    text = re.sub(r"<p(?:\s[^>]*)?>|</p>", "\n", text)
    text = re.sub(r"^(#{1,6} .*?)\s*\n-{3,}\s*$", r"\1", text, flags=re.M)
    text = re.sub(r"^#{1,6}\s*$", "", text, flags=re.M)
    text = convert_quotes(text)
    text = escape_placeholders(text)
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def heading_index(wikis: list[dict], contents: dict[str, str], paths: dict[str, str]) -> dict[str, str]:
    index = {slugify(w["title"]): paths[w["url_slug_full"]] for w in wikis}
    for slug, body in contents.items():
        for heading in re.findall(r"^#{1,6} (.+)$", body, flags=re.M):
            index.setdefault(slugify(heading), paths[slug])
    return index


def rewrite_links(text: str, here: str, paths: dict[str, str], headings: dict[str, str], assets: set[str]) -> str:
    def target(url: str) -> str:
        if url.startswith(UPLOADS):
            name = url[len(UPLOADS):]
            if not vendorable(name):
                return url
            assets.add(name)
            return posixpath.relpath(f"{ASSETS}/{name}", posixpath.dirname(here) or ".")
        match = re.match(r"^(?:https?://(?:www\.)?computerome\.dk)?/?(wiki/)?([^#?]+)(?:#(.*))?$", url)
        if not match or (not match[1] and match[2].rstrip("/") not in paths):
            return f"{SITE}{url}" if url.startswith("/") else url
        match = (None, match[2], match[3])
        slug, anchor = match[1].rstrip("/"), match[2]
        slug = urllib.request.unquote(urllib.request.unquote(slug)).replace("(", "").replace(")", "")
        if slug == "user-guide" and anchor in headings:
            dest, anchor = headings[anchor], anchor
        elif slug in paths:
            dest = paths[slug]
        elif "/" in slug and slug.rsplit("/", 1)[0] in paths:
            parent, sub = slug.rsplit("/", 1)
            dest, anchor = headings.get(sub, paths[parent]), sub if sub in headings else None
            if not anchor:
                print(f"warning: {here}: no section for {url}", file=sys.stderr)
        else:
            print(f"warning: {here}: unresolved wiki link {url}", file=sys.stderr)
            return f"{SITE}/wiki/{slug}"
        rel = posixpath.relpath(dest, posixpath.dirname(here) or ".")
        return f"{rel}#{anchor}" if anchor else rel

    return re.sub(r"(\]\()([^)\s]+)(\))", lambda m: m[1] + target(m[2]) + m[3], text)


def derived_tags(slug: str, title: str) -> list[str]:
    key = f"{slug} {title}".lower()
    tags = []
    if "cloud" in key:
        tags.append("Cloud")
    if any(word in key for word in ("hpc", "slurm", "moab", "running-jobs", "on-demand")):
        tags.append("HPC")
    return tags


def frontmatter(wiki: dict) -> str:
    tags = [t["title"].strip() for t in wiki.get("wiki_tags") or []]
    tags = list(dict.fromkeys(tags + derived_tags(wiki["url_slug_full"], wiki["title"])))
    lines = ["---", f"title: {json.dumps(wiki['title'].strip())}"]
    teaser = " ".join((wiki.get("teaser") or "").split())
    if teaser:
        lines.append(f"description: {json.dumps(teaser)}")
    if tags:
        lines.append("tags:")
        lines += [f"  - {tag}" for tag in tags]
    return "\n".join(lines + ["---", "", ""])


def main() -> None:
    wikis = json.loads(fetch(f"{API}/wikis?pagination[pageSize]=200&populate=*"))["data"]
    wikis = [w for w in wikis if w["url_slug_full"] not in SKIP]
    paths = page_paths(wikis)
    contents = {w["url_slug_full"]: html_to_markdown(w["content"] or "") for w in wikis}
    headings = heading_index(wikis, contents, paths)
    assets: set[str] = set()
    for wiki in wikis:
        slug = wiki["url_slug_full"]
        body = rewrite_links(contents[slug], paths[slug], paths, headings, assets)
        if not re.match(r"^# ", body):
            body = f"# {wiki['title'].strip()}\n\n{body}"
        out = DOCS / paths[slug]
        if out.exists():
            print(f"kept {out} (delete it to re-import)")
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(frontmatter(wiki) + body)
        print(f"wrote {out}")
    for name in sorted(assets):
        out = DOCS / ASSETS / name
        if not out.exists():
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(fetch(UPLOADS + name))
            print(f"downloaded {out}")
