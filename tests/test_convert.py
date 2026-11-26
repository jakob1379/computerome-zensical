import tempfile
from pathlib import Path

from computerome_zensical import escape_placeholders, html_to_markdown, normalize_lists, sync


def test_nested_lists_get_four_space_indent_and_leading_blank_line():
    src = "Intro:\n- a\n  - b\n    ```bash\n    ls\n    ```\n- c\n\nAfter\n"
    assert normalize_lists(src) == (
        "Intro:\n\n- a\n    - b\n        ```bash\n        ls\n        ```\n- c\n\nAfter\n"
    )


def test_normalize_is_idempotent():
    src = "Text\n1. one\n   - nested\n2. two\n"
    once = normalize_lists(src)
    assert normalize_lists(once) == once


def test_titled_div_becomes_admonition():
    src = '<div class="tips">\n<div>\n<span class="title">module avail</span>\n\nList modules.\n</div>\n</div>'
    assert html_to_markdown(src) == '!!! tip "module avail"\n\n    List modules.\n'


def test_note_quote_becomes_admonition():
    src = "> **Note**: Mind the gap.\n> - one\n"
    assert html_to_markdown(src) == "!!! note\n\n    Mind the gap.\n\n    - one\n"


def test_heading_gets_blank_line_but_code_comments_do_not():
    src = "## Login\n!!! tip\n```bash\n# comment\nls\n```\n"
    assert normalize_lists(src) == "## Login\n\n!!! tip\n```bash\n# comment\nls\n```\n"


def test_placeholders_escaped_only_outside_code():
    src = "Use qstat -u <username> or `checkjob <jobid>`\n```bash\nls <dir>\n```\ncd /home/projects/<project-name>/"
    assert escape_placeholders(src) == (
        "Use qstat -u &lt;username&gt; or `checkjob <jobid>`\n```bash\nls <dir>\n```\ncd /home/projects/&lt;project-name&gt;/"
    )


def test_sync_merges_upstream_changes_into_hand_edits():
    with tempfile.TemporaryDirectory() as tmp:
        docs, base = Path(tmp, "docs"), Path(tmp, "upstream")
        upstream = "# Page\n\nIntro.\n\nA\n\nB\n\nC\n\nD\n"
        assert sync({"p.md": upstream, "gone.md": "x\n"}, docs, base) == [("new", "p.md"), ("new", "gone.md")]
        (docs / "p.md").write_text(upstream.replace("Intro.", "!!! tip\n\n    Intro."))
        assert sync({"p.md": upstream, "gone.md": "x\n"}, docs, base) == []

        assert sync({"p.md": upstream.replace("D", "D2")}, docs, base) == [("merged", "p.md"), ("removed", "gone.md")]
        assert (docs / "p.md").read_text() == "# Page\n\n!!! tip\n\n    Intro.\n\nA\n\nB\n\nC\n\nD2\n"
        assert (docs / "gone.md").exists() and not (base / "gone.md").exists()

        assert sync({"p.md": upstream.replace("Intro.", "New intro.").replace("D", "D2")}, docs, base)[0] == ("conflict", "p.md")
        assert "<<<<<<< docs" in (docs / "p.md").read_text()

        docs.joinpath("q.md").write_text("hand written\n")
        assert sync({"q.md": "upstream\n"}, docs, base)[0] == ("baseline", "q.md")
        assert docs.joinpath("q.md").read_text() == "hand written\n"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("ok")
