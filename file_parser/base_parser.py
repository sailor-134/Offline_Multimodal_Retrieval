# 解析器基类
from abc import ABC,abstractmethod
from dataclasses import dataclass
import os

@dataclass
class ParseResult:
    #统一解析结果架构
    success: bool
    content: str = ""
    metadata: dict = None
    error_msg: str = ""

class BaseParser(ABC):
    #统一解析器基类，定义统一接口
    supported_formats = []

    @abstractmethod
    #解析统一文件，返回统一结果
    def parse(self, file_path: str) -> ParseResult:pass

    def extract_base_metadata(self, file_path: str) -> dict:
        #提取通用文件元数据
        stat = os.stat(file_path)
        return{
            "file_name":os.path.basename(file_path),
            "file_path":file_path,
            "file_size":stat.st_size,
            "modify_time":stat.st_mtime,
            "format":os.path.splitext(file_path)[1].lower()
        }
        