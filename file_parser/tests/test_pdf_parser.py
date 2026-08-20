import os
import unittest
from file_parser import ParserFactory, ParseResult

class TestPDFParser(unittest.TestCase):
    def setUp(self):
        self.pdf_path = os.path.abspath("./test_sample/test.pdf")

    def test_normal_parse(self):
        parser = ParserFactory.get_parser(self.pdf_path)
        res: ParseResult = parser.parse(self.pdf_path)
        self.assertIsNotNone(res)
        self.assertTrue(res.success)
        self.assertIsNotNone(res.content)
        self.assertIsNotNone(res.metadata)

    def test_file_not_exist(self):
        fake_path = os.path.abspath("./test_sample/none.pdf")
        parser = ParserFactory.get_parser(fake_path)
        res = parser.parse(fake_path)
        self.assertIsNotNone(res)
        self.assertFalse(res.success)

if __name__ == "__main__":
    unittest.main()