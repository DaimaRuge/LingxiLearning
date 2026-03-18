"""
RAG 服务 - 检索增强生成
"""
from typing import List, Dict, Optional
from .embedding import get_embedding_service
from .vector import get_vector_store
import logging

logger = logging.getLogger(__name__)


class RAGService:
    """RAG 检索增强生成服务"""
    
    def __init__(self):
        self.embedding_service = get_embedding_service()
        self.vector_store = get_vector_store()
    
    def index_document(self, document: Dict) -> str:
        """
        将文档索引到向量库
        
        Args:
            document: {
                "title": str,
                "content": str,
                "chunks": List[str],
                "metadata": dict
            }
        """
        if self.vector_store is None:
            logger.error("Vector store not available")
            return None
        
        doc_id = document.get("title", "unknown")
        chunks = document.get("chunks", [])
        
        if not chunks:
            # 如果没有分块，用全文
            chunks = [document.get("content", "")]
        
        # 向量化
        embeddings = self.embedding_service.encode(chunks)
        
        # 构建 payload
        payloads = [
            {
                "doc_id": doc_id,
                "chunk_index": i,
                "content": chunk,
                "metadata": document.get("metadata", {})
            }
            for i, chunk in enumerate(chunks)
        ]
        
        # 存入向量库
        try:
            self.vector_store.create_collection()
            ids = [f"{doc_id}_{i}" for i in range(len(chunks))]
            self.vector_store.add_vectors(embeddings, payloads, ids)
            logger.info(f"Indexed document: {doc_id}, {len(chunks)} chunks")
            return doc_id
        except Exception as e:
            logger.error(f"Failed to index document: {e}")
            return None
    
    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        检索相关文档块
        
        Args:
            query: 查询文本
            top_k: 返回数量
            
        Returns:
            检索结果列表
        """
        if self.vector_store is None:
            logger.error("Vector store not available")
            return []
        
        # 向量化查询
        query_embedding = self.embedding_service.encode(query)
        
        # 检索
        results = self.vector_store.search(query_embedding, top_k=top_k)
        
        return results
    
    def generate_answer(
        self,
        query: str,
        context: Optional[List[Dict]] = None
    ) -> Dict:
        """
        生成回答（需要接入 LLM）
        
        Args:
            query: 用户问题
            context: 上下文（检索结果）
            
        Returns:
            {
                "answer": str,
                "references": List[Dict]
            }
        """
        if context is None:
            context = self.retrieve(query)
        
        # 构建 prompt（简化版）
        context_text = "\n\n".join([
            f"[{i+1}] {item['payload']['content']}"
            for i, item in enumerate(context)
        ])
        
        prompt = f"""基于以下参考资料回答问题。如果参考资料中没有相关信息，请说明。

参考资料：
{context_text}

问题：{query}

回答："""
        
        # TODO: 接入 LLM API
        # 这里先返回 prompt 作为演示
        return {
            "answer": f"[LLM 待接入] 这个问题需要调用 GLM-5 API 来回答。检索到 {len(context)} 条相关资料。",
            "prompt": prompt,
            "references": context
        }


# 全局单例
_rag_service = None


def get_rag_service() -> RAGService:
    """获取 RAG 服务单例"""
    global _rag_service
    if _rag_service is None:
        _rag_service = RAGService()
    return _rag_service
