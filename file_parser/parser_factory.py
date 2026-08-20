# 解析器工厂
import os
from .base_parser import BaseParser, ParseResult
from .txt_parser import TXTParser
from .pdf_parser import PDFParser
from .docx_parser import DOCXParser
from .image_parser import ImageParser

class ParserFactory:
    #分配解析器
    _parser_map = {}

    @classmethod
    def register_parser(cls, parser_cls):
        #注册解析器
        for fmt in parser_cls.supported_formats:
            cls._parser_map[fmt] = parser_cls()

    @classmethod
    def get_parser(cls, file_path: str):
        ext = os.path.splitext(file_path)[1].lower()
        return cls._parser_map.get(ext)

    @classmethod
    def parse_file(cls, file_path: str) -> ParseResult:
        #单文件统一解析入口
        parser = cls.get_parser(file_path)
        if not parser:
            return ParseResult(success=False, error_msg=f"不支持的文件格式: {file_path}")
        try:
            return parser.parse(file_path)
        except Exception as e:
            return ParseResult(success=False, error_msg=f"解析失败: {str(e)}")

# 启动时自动注册所有解析器
ParserFactory.register_parser(TXTParser)
ParserFactory.register_parser(PDFParser)
ParserFactory.register_parser(DOCXParser)
ParserFactory.register_parser(ImageParser)