"""
向量化服务
使用 BGE 模型进行文本向量化
"""
from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np
import logging

logger = logging.getLogger(__name__)


class EmbeddingService:
    """文本向量化服务"""
    
    def __init__(self, model_name: str = "BAAI/bge-large-zh-v1.5"):
        self.model_name = model_name
        self.model = None
        self._load_model()
    
    def _load_model(self):
        """加载模型"""
        logger.info(f"Loading embedding model: {self.model_name}")
        self.model = SentenceTransformer(self.model_name)
        logger.info("Embedding model loaded successfully")
    
    def encode(self, texts: List[str], normalize: bool = True) -> np.ndarray:
        """
        将文本列表转为向量
        
        Args:
            texts: 文本列表
            normalize: 是否归一化
            
        Returns:
            numpy array of embeddings
        """
        if isinstance(texts, str):
            texts = [texts]
        
        embeddings = self.model.encode(
            texts,
            normalize_embeddings=normalize,
            show_progress_bar=False
        )
        
        return embeddings
    
    def get_dimension(self) -> int:
        """获取向量维度"""
        return self.model.get_sentence_embedding_dimension()


# 全局单例
_embedding_service = None


def get_embedding_service() -> EmbeddingService:
    """获取向量化服务单例"""
    global _embedding_service
    if _embedding_service is None:
        _embedding_service = EmbeddingService()
    return _embedding_service


def encode_texts(texts: List[str]) -> np.ndarray:
    """便捷函数"""
    service = get_embedding_service()
    return service.encode(texts)
