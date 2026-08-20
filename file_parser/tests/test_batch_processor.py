import os
import unittest
import shutil
from file_parser import BatchProcessor

class TestBatchProcessor(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_batch_dir"
        os.makedirs(self.test_dir, exist_ok=True)
        #创建2个支持格式文件 + 1个不支持格式文件
        with open(os.path.join(self.test_dir, "a.txt"), "w", encoding="utf-8") as f:
            f.write("文件A")
        with open(os.path.join(self.test_dir, "b.txt"), "w", encoding="utf-8") as f:
            f.write("文件B")
        with open(os.path.join(self.test_dir, "c.xxx"), "w") as f:
            f.write("不支持格式")

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_process_directory(self):
        results = BatchProcessor.process_directory(self.test_dir)
        self.assertEqual(len(results), 3)
        success_count = sum(1 for r in results if r.success)
        self.assertEqual(success_count, 2)

    def test_get_supported_files(self):
        files = BatchProcessor.get_supported_files(self.test_dir)
        self.assertEqual(len(files), 2)

if __name__ == "__main__":
    unittest.main()