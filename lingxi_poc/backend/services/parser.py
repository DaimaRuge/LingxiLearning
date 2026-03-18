"""
文档解析服务
支持 PDF, EPUB, Markdown, TXT 等格式
"""
import fitz  # PyMuPDF
from pathlib import Path
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)


class DocumentParser:
    """文档解析器"""
    
    SUPPORTED_FORMATS = {'.pdf', '.epub', '.md', '.txt'}
    
    def __init__(self):
        self.chunk_size = 500
        self.chunk_overlap = 50
    
    def parse(self, file_path: str) -> Dict:
        """
        解析文档
        
        Returns:
            {
                "title": str,
                "content": str,
                "chunks": List[str],
                "metadata": dict
            }
        """
        path = Path(file_path)
        suffix = path.suffix.lower()
        
        if suffix == '.pdf':
            return self._parse_pdf(file_path)
        elif suffix == '.epub':
            return self._parse_epub(file_path)
        elif suffix == '.md':
            return self._parse_markdown(file_path)
        elif suffix == '.txt':
            return self._parse_txt(file_path)
        else:
            raise ValueError(f"Unsupported format: {suffix}")
    
    def _parse_pdf(self, file_path: str) -> Dict:
        """解析 PDF"""
        doc = fitz.open(file_path)
        text_parts = []
        
        for page in doc:
            text = page.get_text()
            if text.strip():
                text_parts.append(text)
        
        content = "\n\n".join(text_parts)
        chunks = self._split_into_chunks(content)
        
        return {
            "title": Path(file_path).stem,
            "content": content,
            "chunks": chunks,
            "metadata": {
                "pages": len(doc),
                "format": "pdf"
            }
        }
    
    def _parse_epub(self, file_path: str) -> Dict:
        """解析 EPUB（简化版）"""
        # TODO: 实现 EPUB 解析
        return {
            "title": Path(file_path).stem,
            "content": "",
            "chunks": [],
            "metadata": {"format": "epub"}
        }
    
    def _parse_markdown(self, file_path: str) -> Dict:
        """解析 Markdown"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        chunks = self._split_into_chunks(content)
        
        return {
            "title": Path(file_path).stem,
            "content": content,
            "chunks": chunks,
            "metadata": {"format": "md"}
        }
    
    def _parse_txt(self, file_path: str) -> Dict:
        """解析 TXT"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        chunks = self._split_into_chunks(content)
        
        return {
            "title": Path(file_path).stem,
            "content": content,
            "chunks": chunks,
            "metadata": {"format": "txt"}
        }
    
    def _split_into_chunks(self, text: str) -> List[str]:
        """将文本分割成块"""
        # 简单的滑动窗口分块
        chunks = []
        start = 0
        text_len = len(text)
        
        while start < text_len:
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk.strip())
            start = end - self.chunk_overlap
        
        return [c for c in chunks if c]


def parse_document(file_path: str) -> Dict:
    """解析文档的便捷函数"""
    parser = DocumentParser()
    return parser.parse(file_path)
