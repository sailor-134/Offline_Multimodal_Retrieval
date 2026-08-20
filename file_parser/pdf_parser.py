# PDF解析器
import pypdfium2 as pdfium
from .base_parser import BaseParser, ParseResult

class PDFParser(BaseParser):
    supported_formats = ['.pdf']

    def parse(self, file_path: str) -> ParseResult:
        try:
            metadata = self.extract_base_metadata(file_path)
            pdf = pdfium.PdfDocument(file_path)
            text_list = []
            for page in pdf:
                text_page = page.get_textpage()
                text_list.append(text_page.get_text_range())
            content = '\n'.join(text_list)
            pdf.close()
            return ParseResult(success=True, content=content,metadata=metadata)
        except Exception as e:
            return ParseResult(success=False, error_msg=f"PDF解析失败：{str(e)}")

