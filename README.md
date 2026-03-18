# 灵犀智读 - 个人终身学习数字读书系统

> 🧠 首款基于大模型 Agent 的个人终身学习数字伴侣

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-green.svg)]()
[![Version](https://img.shields.io/badge/version-0.2.0-green.svg)]()

---

## 📖 产品简介

**灵犀智读**是一款基于大模型 Agent 的个人终身学习数字读书系统。

```
不是给你的大脑扩容，而是给你的思维建索引
不是帮你读更多书，而是让你读过的书都记住
不是替代你思考，而是放大你的思考能力
```

---

## 🎯 核心功能

| 模块 | 功能 | 状态 |
|------|------|------|
| M1 | 分布式文档索引与关系重构 | 🚧 开发中 |
| M2 | 知识网络扩展与完善 | 🚧 开发中 |
| M3 | 学习与创作辅助 | 🚧 开发中 |
| M4 | 个人终身学习伴侣 | 🚧 开发中 |
| M5 | 课程规划与内容生成 | 📋 规划中 |

### 核心特性 (POC 阶段)

- 📚 **文档解析** - PDF/EPUB/MD/TXT 多格式支持
- 🔍 **向量检索** - BGE 中文向量化 + Qdrant 存储
- 🤖 **RAG 对话** - 基于检索的 AI 问答
- 🗂️ **知识图谱** - 规划中
- 📈 **成长追踪** - 规划中

---

## 🏗️ 技术架构

```
用户交互层：React + Electron + Flutter
    ↓
Agent 服务层：OpenClaw-style Framework
    ↓
知识服务层：Neo4j + Milvus + PostgreSQL
    ↓
基础模型层：GLM-5 / GPT-4 + BGE + LLaVA
```

### POC 技术栈

| 组件 | 技术 | 状态 |
|------|------|------|
| Web UI | Streamlit | 🚧 开发中 |
| 后端 | FastAPI | 🚧 开发中 |
| 向量数据库 | Qdrant | ✅ 就绪 |
| Embedding | BGE-large-zh | ✅ 就绪 |
| LLM | GLM-5 | 🚧 接入中 |
| 文档解析 | PyMuPDF | ✅ 就绪 |

---

## 📂 文档结构

```
LingxiLearning/
├── Version1/           # 需求与调研
│   ├── 01_需求深度分析.md
│   ├── 02_竞品分析与市场研究.md
│   ├── 03_技术调研报告.md
│   └── 04_V1产品概览.md
├── Version2/           # 原型与商业
│   ├── 01_产品原型设计.md
│   ├── 02_商业模式细化.md
│   └── 03_V2产品概览.md
├── Version3/           # 正式规格
│   ├── 01_产品规格说明书.md
│   └── 02_V3产品概览.md
└── README.md           # 本文件
```

---

## 🚀 里程碑

| 阶段 | 时间 | 目标 |
|------|------|------|
| MVP | Month 3 | 文档索引 + AI 对话 + 知识图谱 |
| Pro | Month 6 | 个人 AI 伴侣 + 学习路径 |
| Enterprise | Month 9 | 企业知识库 + Agent 生成平台 |

---

## 💡 竞品分析

| 产品 | 定位 | 本产品差异 |
|------|------|------------|
| Notion | All-in-One 工作空间 | 知识图谱 + AI 伴侣 |
| Zotero | 学术文献管理 | AI 辅助 + 记忆系统 |
| Obsidian | 双链笔记 | 多端 + AI 原生 |
| ChatGPT | AI 对话 | 个人知识库 + 持久记忆 |

---

## 📊 市场机会

| 细分市场 | 规模 | 增长率 |
|----------|------|--------|
| 个人知识库 | $2B | 30% CAGR |
| AI 教育 | $6B | 40% CAGR |
| 知识管理 | $4.5B | 15% CAGR |

---

## 🛠️ 开发指南

### 本地开发

```bash
# 克隆项目
git clone https://github.com/DaimaRuge/LingxiLearning.git

# 安装依赖
cd lingxi_poc
pip install -r requirements.txt

# 启动 Qdrant (Docker)
docker run -d -p 6333:6333 qdrant/qdrant

# 运行 Streamlit UI
streamlit run lingxi_poc/app.py
```

### 项目结构

```
lingxi_poc/
├── backend/
│   ├── services/
│   │   ├── parser.py       # 文档解析
│   │   ├── embedding.py     # 向量化
│   │   ├── vector.py       # 向量存储
│   │   └── rag.py          # RAG 核心
│   └── config.py           # 配置
├── requirements.txt
└── README.md
```

---

## 📁 文档结构

```
LingxiLearning/
├── README.md           # 项目主页
├── CHANGELOG.md        # 更新日志
├── CONTRIBUTING.md      # 贡献指南
├── LICENSE             # MIT 许可证
├── docs/               # 项目文档
│   ├── API接口文档.md
│   └── POC实现计划.md
├── Version1/           # V1.0 需求调研
├── Version2/           # V2.0 产品设计
├── Version3/           # V3.0 技术规格
└── lingxi_poc/         # POC 代码框架
    └── backend/
        └── services/   # 核心服务
```

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 📧 联系方式

- **GitHub Issues**: [DaimaRuge/LingxiLearning Issues](https://github.com/DaimaRuge/LingxiLearning/issues)
- **邮箱**: 待定

---

*让每个人都拥有自己的"知识图书馆"和"AI 学习伴侣"*
