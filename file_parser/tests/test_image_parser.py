import os
import unittest
from PIL import Image
from file_parser import ParserFactory

class TestImageParser(unittest.TestCase):
    def setUp(self):
        self.test_file = os.path.abspath("test_sample.png")
        img = Image.new('RGB', (100, 100), color='red')
        img.save(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_normal_parse(self):
        parser = ParserFactory.get_parser(self.test_file)
        result = parser.parse(self.test_file)
        self.assertTrue(result.success)
        self.assertEqual(result.metadata["format"], ".png")
        self.assertEqual(result.metadata["width"], 100)
        self.assertEqual(result.metadata["height"], 100)

    def test_file_not_exist(self):
        fake_path = os.path.abspath("not_exist.png")
        parser = ParserFactory.get_parser(fake_path)
        result = parser.parse(fake_path)
        self.assertFalse(result.success)

if __name__ == "__main__":
    unittest.main()