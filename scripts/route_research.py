"""Offline research-entry helper; the index owns aliases, not this script."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TARGET = "skills/research/web-research/SKILL.md"

def aliases(root=ROOT):
    lines = (root / "SKILLS_INDEX.md").read_text(encoding="utf-8").splitlines()
    rows = [line for line in lines if line.startswith("- ") and
            line.endswith("→ `" + TARGET + "`")]
    if len(rows) != 1:
        raise ValueError("Expected one canonical research alias row")
    return [word.strip().casefold() for word in
            rows[0][2:].split(" → ", 1)[0].split("、")]

def route(text, root=ROOT):
    normalized = re.sub(r"\s+", " ", text).strip().casefold()
    # Conservative whole-request suppression; mixed intent needs contextual routing.
    if re.search(r"不要联网|不用联网|不联网|禁止联网|不要搜索|不用搜索|仅本地|只搜索本地|只查本地|"
                 r"别联网|别搜索|离线|do not (?:search|browse)|don['’]t (?:search|browse)", normalized):
        return None
    if re.search(r"本地|仓库(?:代码|文件)|聊天记录|表格(?:内|中)|"
                 r"local files?|repository code|chat history", normalized):
        return None
    if re.search(r"(?:搜索|anysearch|any search)(?:是什么|什么意思)|what is anysearch", normalized):
        return None
    for alias in aliases(root):
        pattern = re.escape(alias)
        if alias.isascii():
            pattern = r"(?<![a-z0-9_])" + pattern + r"(?![a-z0-9_])"
        if re.search(pattern, normalized):
            return TARGET
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    args = parser.parse_args()
    print(json.dumps({"skill": route(args.query)}, ensure_ascii=False))
