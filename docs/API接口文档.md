# API 接口文档

> **版本：** V1.0  
> **日期：** 2026-03-19

---

## 一、接口概述

### 1.1 基础信息

| 项目 | 说明 |
|------|------|
| 基础 URL | `https://api.lingxi.ai/v1` |
| 认证方式 | Bearer Token (JWT) |
| 数据格式 | JSON |
| 字符编码 | UTF-8 |

### 1.2 通用响应格式

```json
{
  "code": 0,
  "message": "success",
  "data": {}
}
```

### 1.3 错误码定义

| 错误码 | 说明 |
|--------|------|
| 0 | 成功 |
| 1001 | 参数错误 |
| 1002 | 认证失败 |
| 1003 | 权限不足 |
| 2001 | 文档不存在 |
| 2002 | 文档解析失败 |
| 3001 | AI 服务异常 |
| 3002 | AI 服务超时 |

---

## 二、文档管理接口

### 2.1 导入文档

**接口：** `POST /documents`

**请求：**
```json
{
  "title": "深度学习论文",
  "file_type": "pdf",
  "content": "base64编码的文件内容",
  "metadata": {
    "author": "作者名",
    "tags": ["AI", "深度学习"]
  }
}
```

**响应：**
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "document_id": "doc_abc123",
    "title": "深度学习论文",
    "status": "indexing",
    "created_at": "2026-03-19T10:00:00Z"
  }
}
```

### 2.2 获取文档列表

**接口：** `GET /documents`

**参数：**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| page | int | 否 | 页码，默认 1 |
| page_size | int | 否 | 每页数量，默认 20 |
| keyword | string | 否 | 搜索关键词 |

**响应：**
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "total": 100,
    "page": 1,
    "page_size": 20,
    "documents": [
      {
        "document_id": "doc_abc123",
        "title": "深度学习论文",
        "file_type": "pdf",
        "created_at": "2026-03-19T10:00:00Z",
        "status": "indexed"
      }
    ]
  }
}
```

### 2.3 获取文档详情

**接口：** `GET /documents/{document_id}`

**响应：**
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "document_id": "doc_abc123",
    "title": "深度学习论文",
    "file_type": "pdf",
    "content": "文档文本内容...",
    "chunks": [
      {
        "chunk_id": "chunk_001",
        "content": "第一段内容...",
        "index": 0
      }
    ],
    "metadata": {
      "author": "作者名",
      "tags": ["AI", "深度学习"],
      "page_count": 20
    },
    "created_at": "2026-03-19T10:00:00Z",
    "updated_at": "2026-03-19T10:30:00Z"
  }
}
```

### 2.4 对文档提问

**接口：** `POST /documents/{document_id}/chat`

**请求：**
```json
{
  "question": "这篇论文的主要贡献是什么？",
  "mode": "rag"
}
```

**响应：**
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "answer": "这篇论文的主要贡献是提出了...",
    "references": [
      {
        "chunk_id": "chunk_001",
        "content": "引用内容...",
        "score": 0.95
      }
    ]
  }
}
```

---

## 三、知识图谱接口

### 3.1 获取全局图谱

**接口：** `GET /graph`

**参数：**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| depth | int | 否 | 扩展深度，默认 2 |

**响应：**
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "nodes": [
      {
        "id": "node_001",
        "label": "深度学习",
        "type": "concept",
        "properties": {}
      }
    ],
    "edges": [
      {
        "source": "node_001",
        "target": "node_002",
        "relation": "cites"
      }
    ]
  }
}
```

### 3.2 获取相关节点

**接口：** `GET /graph/related/{node_id}`

**响应：**
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "nodes": [...],
    "edges": [...]
  }
}
```

---

## 四、AI 伴侣接口

### 4.1 对话

**接口：** `POST /companion/chat`

**请求：**
```json
{
  "message": "我想学习机器学习，应该从哪里开始？",
  "context": true
}
```

**响应：**
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "reply": "学习机器学习，建议从以下路径开始...",
    "suggestions": [
      {
        "type": "learning_path",
        "title": "机器学习入门路径",
        "items": ["线性代数", "概率统计", "Python", "机器学习基础"]
      }
    ]
  }
}
```

### 4.2 获取记忆

**接口：** `GET /companion/memory`

**参数：**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| type | string | 否 | memory/episodic/semantic |

**响应：**
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "memory": [
      {
        "id": "mem_001",
        "content": "用户对深度学习特别感兴趣",
        "type": "semantic",
        "created_at": "2026-03-19T10:00:00Z"
      }
    ]
  }
}
```

---

## 五、附录

### 5.1 SDK 示例

**Python SDK：**
```python
from lingxi import LingxiClient

client = LingxiClient(api_key="your_api_key")

# 导入文档
doc = client.documents.create(
    title="深度学习",
    file_type="pdf",
    content=pdf_content
)

# 对话
response = client.companion.chat("机器学习怎么入门？")
print(response.reply)
```

---

*本文档持续更新中...*
