# TXT 解析器
from .base_parser import BaseParser, ParseResult

class TXTParser(BaseParser):
    supported_formats = [".txt"]

    def parse(self, file_path: str) -> ParseResult:
        try:
            metadata = self.extract_base_metadata(file_path)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(file_path, 'r', encoding='gbk') as f:
                    content = f.read()
            return ParseResult(success=True, content=content,metadata=metadata)
        except Exception as e:
            return ParseResult(success=False, error_msg=f"TXT解析失败：{str(e)}")

