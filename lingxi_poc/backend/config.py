"""
灵犀智读 - POC 核心配置
"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GLM_API_KEY = os.getenv("GLM_API_KEY", "your_glm_api_key")

# 向量数据库配置
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))
COLLECTION_NAME = "lingxi_documents"

# 文档处理配置
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Embedding 配置
EMBEDDING_MODEL = "BAAI/bge-large-zh-v1.5"
EMBEDDING_DIM = 1024

# LLM 配置
LLM_MODEL = "glm-5"
LLM_TEMPERATURE = 0.7
LLM_MAX_TOKENS = 2048

# 图谱配置
MAX_GRAPH_NODES = 1000
GRAPH_DEPTH = 3
