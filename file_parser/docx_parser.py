# DOCX解析器
from docx import Document
from .base_parser import BaseParser, ParseResult

class DOCXParser(BaseParser):
    supported_formats = ['.docx']

    def parse(self, file_path: str) -> ParseResult:
        try:
            metadata = self.extract_base_metadata(file_path)
            doc = Document(file_path)
            paragraphs = [para.text for para in doc.paragraphs]
            content = '\n'.join(paragraphs)
            return ParseResult(success=True, content=content, metadata=metadata)
        except Exception as e:
            return ParseResult(success=False, error_msg=f"DOCX解析失败：{str(e)}")