#!/usr/bin/env python3
"""Validate generated standalone HTML artifacts."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REMOTE_SRC_RE = re.compile(
    r"""src\s*=\s*["'](?:https?:)?//""",
    re.IGNORECASE,
)
REMOTE_LINK_DEP_RE = re.compile(
    r"""<link\b[^>]*href\s*=\s*["'](?:https?:)?//""",
    re.IGNORECASE,
)
LONG_CODELIKE_TOKEN_RE = re.compile(
    r"\b[A-Za-z0-9][A-Za-z0-9_./:-]{24,}\b",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def warn(message: str) -> None:
    print(f"WARN: {message}")


def strip_tags(html: str) -> str:
    html = re.sub(r"<script\b[^>]*>.*?</script>", " ", html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r"<style\b[^>]*>.*?</style>", " ", html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", html).strip()


def extract_styles(html: str) -> str:
    return "\n".join(
        match.group(1)
        for match in re.finditer(
            r"<style\b[^>]*>(.*?)</style>",
            html,
            flags=re.IGNORECASE | re.DOTALL,
        )
    )


def resolve_html_file(path: Path) -> Path | None:
    if path.is_file():
        return path
    if path.is_dir():
        html_files = sorted(path.glob("*.html"))
        if len(html_files) != 1:
            fail(f"expected exactly one .html file in directory, found {len(html_files)}")
            return None
        return html_files[0]
    fail(f"path does not exist: {path}")
    return None


def validate(path: Path) -> int:
    html_file = resolve_html_file(path)
    if html_file is None:
        return 1

    errors = 0
    text = html_file.read_text(encoding="utf-8")
    lower = text.lower()
    styles = extract_styles(text).lower()
    visible_text = strip_tags(text)

    checks = [
        (html_file.suffix.lower() == ".html", "file extension must be .html"),
        (lower.lstrip().startswith("<!doctype html>"), "file must start with <!doctype html>"),
        ("<meta name=\"viewport\"" in lower or "<meta name='viewport'" in lower, "missing viewport meta tag"),
        ("<title>" in lower and "</title>" in lower, "missing title tag"),
        ("<style" in lower and "</style>" in lower, "missing inline style block"),
        ("```" not in text, "html file contains markdown code fences"),
        (not REMOTE_SRC_RE.search(text) and not REMOTE_LINK_DEP_RE.search(text), "external resource dependency found"),
    ]

    for ok, message in checks:
        if not ok:
            fail(message)
            errors += 1

    if "@media" not in text:
        warn("no responsive @media rule found")
    if len(visible_text) < 400:
        warn("body text appears sparse; confirm the artifact is useful")
    if "<script" in lower and "addEventListener" not in text and "onclick" not in lower:
        warn("script block found but no obvious interaction handler")
    if ("display: grid" in styles or "display:flex" in styles or "display: flex" in styles) and "min-width: 0" not in styles:
        warn("grid/flex layout found without min-width: 0; nested cards or long text may overflow parent borders")
    if LONG_CODELIKE_TOKEN_RE.search(visible_text) and "overflow-wrap" not in styles and "word-break" not in styles:
        warn("long code-like text found without overflow-wrap/word-break; identifiers, URLs, or commands may clip")
    if ("flow" in lower or "diagram" in lower) and "repeat(3" in styles and "auto-fit" not in styles:
        warn("dense flow/diagram grid uses fixed 3-column repeat without auto-fit; check narrow-width clipping")

    if errors:
        print(f"Validation failed: {errors} error(s) in {html_file}")
        return 1

    print(f"Validation passed: {html_file}")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_html_artifact.py <html-file-or-directory>")
        return 2
    return validate(Path(argv[1]))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
