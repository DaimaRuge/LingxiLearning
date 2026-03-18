"""
向量存储与检索服务
使用 Qdrant 向量数据库
"""
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from qdrant_client.http.exceptions import UnexpectedResponse
from typing import List, Dict, Optional, Tuple
import numpy as np
import uuid
import logging

logger = logging.getLogger(__name__)


class VectorStore:
    """向量存储服务"""
    
    def __init__(self, host: str = "localhost", port: int = 6333):
        self.client = QdrantClient(host=host, port=port)
        self.collection_name = "lingxi_documents"
        self.vector_size = 1024  # bge-large-zh-v1.5 维度
    
    def create_collection(self, recreate: bool = False):
        """创建 Collection"""
        try:
            self.client.get_collection(self.collection_name)
            if recreate:
                logger.info(f"Deleting existing collection: {self.collection_name}")
                self.client.delete_collection(self.collection_name)
            else:
                logger.info(f"Collection {self.collection_name} already exists")
                return
        except (UnexpectedResponse, Exception):
            pass
        
        logger.info(f"Creating collection: {self.collection_name}")
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=self.vector_size,
                distance=Distance.COSINE
            )
        )
        logger.info(f"Collection {self.collection_name} created successfully")
    
    def add_vectors(
        self,
        vectors: np.ndarray,
        payloads: List[Dict],
        ids: Optional[List[str]] = None
    ) -> List[str]:
        """
        添加向量
        
        Args:
            vectors: 向量数组 (N, D)
            payloads: 元数据列表
            ids: ID 列表，默认自动生成
            
        Returns:
            生成的 ID 列表
        """
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in range(len(vectors))]
        
        points = [
            PointStruct(
                id=id_,
                vector=vector.tolist() if isinstance(vector, np.ndarray) else vector,
                payload=payload
            )
            for id_, vector, payload in zip(ids, vectors, payloads)
        ]
        
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
        
        logger.info(f"Added {len(points)} vectors to {self.collection_name}")
        return ids
    
    def search(
        self,
        query_vector: np.ndarray,
        top_k: int = 5,
        filter_conditions: Optional[Dict] = None
    ) -> List[Dict]:
        """
        向量检索
        
        Args:
            query_vector: 查询向量
            top_k: 返回数量
            filter_conditions: 过滤条件
            
        Returns:
            检索结果列表
        """
        search_params = {"limit": top_k}
        
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector.tolist() if isinstance(query_vector, np.ndarray) else query_vector,
            search_params=search_params,
            query_filter=filter_conditions
        )
        
        return [
            {
                "id": result.id,
                "score": result.score,
                "payload": result.payload
            }
            for result in results
        ]
    
    def delete(self, point_ids: List[str]):
        """删除向量"""
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=point_ids
        )
        logger.info(f"Deleted {len(point_ids)} vectors")


# 全局单例
_vector_store = None


def get_vector_store() -> VectorStore:
    """获取向量存储单例"""
    global _vector_store
    if _vector_store is None:
        _vector_store = VectorStore()
    except Exception as e:
        logger.error(f"Failed to connect to vector store: {e}")
        return None
    return _vector_store
