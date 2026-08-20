# 批量处理工具
import os
from .parser_factory import ParserFactory
from .base_parser import ParseResult
from typing import List

class BatchProcessor:
    @staticmethod
    def process_directory(dir_path: str) -> List[ParseResult]:
        #遍历目录，批量解析支持文件
        results = []
        if not os.path.isdir(dir_path):
            return [ParseResult(success=False, error_msg=f"目录不存在: {dir_path}")]
        
        for root, _, files in os.walk(dir_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                result = ParserFactory.parse_file(file_path)
                results.append(result)
        return results

    @staticmethod
    def get_supported_files(dir_path: str) -> List[str]:
        #获取目录下支持文件路径
        file_list = []
        if not os.path.isdir(dir_path):
            return []
        for root, _, files in os.walk(dir_path):
            for file_name in files:
                ext = os.path.splitext(file_name)[1].lower()
                if ext in ['.txt', '.pdf', '.docx', '.jpg', '.jpeg', '.png']:
                    file_list.append(os.path.join(root, file_name))
        return file_list