# 图片解析器
from PIL import Image
from .base_parser import BaseParser,ParseResult

class ImageParser(BaseParser):
    supported_formats = ['.jpg','.jpeg','.png']

    def parse(self, file_path: str) -> ParseResult:
        try:
            metadata = self.extract_base_metadata(file_path)
            #优先提取元数据
            with Image.open(file_path) as img:
                metadata['width'] = img.width
                metadata['height'] = img.height
                metadata['mode'] = img.mode
            return ParseResult(success=True, content="",metadata=metadata)
        except Exception as e:
            return ParseResult(success=False, error_msg=f"图片解析失败：{str(e)}")

