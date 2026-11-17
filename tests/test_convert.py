from computerome_zensical import escape_placeholders, html_to_markdown, normalize_lists


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


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("ok")
