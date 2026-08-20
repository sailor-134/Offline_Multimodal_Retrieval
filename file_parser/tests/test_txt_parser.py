import os
import unittest
from file_parser import ParserFactory

class TestTXTParser(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_sample.txt"
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("这是TXT测试文本\n用于验证TXT解析功能")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_normal_parse(self):
        result = ParserFactory.parse_file(self.test_file)
        self.assertTrue(result.success)
        self.assertIn("测试文本", result.content)
        self.assertEqual(result.metadata["format"], ".txt")

    def test_file_not_exist(self):
        result = ParserFactory.parse_file("not_exist.txt")
        self.assertFalse(result.success)

    def test_unsupported_format(self):
        result = ParserFactory.parse_file("test.xxx")
        self.assertFalse(result.success)

if __name__ == "__main__":
    unittest.main()