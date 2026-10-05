"""Offline routing contracts; no API calls or model-routing assertions."""
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("route_research", ROOT / "scripts/route_research.py")
router = importlib.util.module_from_spec(spec)
spec.loader.exec_module(router)

class ResearchRouting(unittest.TestCase):
    def test_positive_requests(self):
        for query in [
            "搜索", "查资料", "联网检索", "帮我搜索调酒台厂家",
            "搜一下304不锈钢", "查资料比较201和304", "联网搜索最新厂家电话",
            "帮我上网查官网", "网上查一下", "网页检索技术文档",
            "资料调研", "核验来源", "用anysearch查厂家", "ANYSEARCH 最新资料",
            "any search 调酒柜", "any   search 最新资料",
        ]:
            with self.subTest(query=query):
                self.assertEqual(router.route(query), router.TARGET)

    def test_exclusions(self):
        for query in [
            "不要联网，帮我搜索", "不用联网查资料", "不联网搜索",
            "禁止联网检索", "不要搜索", "不用搜索", "仅本地查资料",
            "只搜索本地文件", "只查本地资料", "别联网搜索", "离线搜索",
            "搜索本地文件", "搜索仓库代码", "搜索聊天记录", "搜索表格内内容",
            "don't search with anysearch", "do not browse with anysearch",
            "anysearch local files", "anysearch repository code",
            "搜索是什么意思", "anysearch是什么", "what is anysearch",
            "manysearch", "anysearching", "帮我算体积", "",
        ]:
            with self.subTest(query=query):
                self.assertIsNone(router.route(query))

    def test_all_index_paths_exist(self):
        index = (ROOT / "SKILLS_INDEX.md").read_text(encoding="utf-8")
        paths = re.findall(r"`(skills/[^\`]+/SKILL.md)`", index)
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file())

    def test_alias_and_frontmatter_contract(self):
        skill = (ROOT / router.TARGET).read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\nname: web-research\ndescription:"))
        description = skill.split("---", 2)[1]
        for alias in router.aliases():
            with self.subTest(alias=alias):
                self.assertIn(alias, description)
        for command in ("search", "batch_search", "extract", "get_sub_domains"):
            self.assertIn("<cmd> " + command, skill)
        self.assertIn("https://github.com/anysearch-ai/anysearch-skill", skill)

if __name__ == "__main__":
    unittest.main()
