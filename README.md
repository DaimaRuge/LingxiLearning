# 灵犀智读 - 个人终身学习数字读书系统

> 🧠 首款基于大模型 Agent 的个人终身学习数字伴侣

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-green.svg)]()
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)]()
[![Version](https://img.shields.io/badge/version-0.3.0-green.svg)]()

---

## 📖 产品简介

**灵犀智读**是一款基于大模型 Agent 的个人终身学习数字读书系统。

```
不是给你的大脑扩容，而是给你的思维建索引
不是帮你读更多书，而是让你读过的书都记住
不是替代你思考，而是放大你的思考能力
```

---

## 🚀 快速启动

### 前置要求

- Python 3.10+
- Docker Desktop (用于 Qdrant 向量数据库)

### 启动步骤

```bash
# 1. 克隆项目
git clone https://github.com/DaimaRuge/LingxiLearning.git
cd LingxiLearning/lingxi_poc

# 2. 启动 Qdrant 向量数据库
docker run -d -p 6333:6333 qdrant/qdrant

# 3. 安装依赖
pip install -r requirements.txt

# 4. 启动应用
streamlit run app.py

# 5. 打开浏览器
# 访问 http://localhost:8501
```

### Windows 用户

直接双击运行 `start.bat`

---

## 🎯 MVP 功能 (Demo)

| 功能 | 说明 | 状态 |
|------|------|------|
| 📖 文档导入 | 支持 PDF/TXT/MD | ✅ 可用 |
| 🔍 文档解析 | 文本提取与分块 | ✅ 可用 |
| 💬 AI 对话 | 基于 RAG 的问答 | 🚧 待接入 GLM |
| 🗺️ 知识图谱 | 可视化知识网络 | 📋 规划中 |

---

## 📂 项目结构

```
LingxiLearning/
├── README.md              # 项目主页
├── CHANGELOG.md          # 更新日志
├── LICENSE               # MIT 许可证
├── docs/                 # 项目文档
│   ├── API接口文档.md
│   └── POC实现计划.md
├── Version1/             # V1.0 需求调研
├── Version2/             # V2.0 产品设计
├── Version3/             # V3.0 技术规格
└── lingxi_poc/          # MVP Demo 代码
    ├── app.py            # Streamlit Web UI
    ├── start.bat         # Windows 启动脚本
    ├── requirements.txt   # Python 依赖
    ├── env.example       # 环境变量示例
    └── backend/
        ├── config.py      # 配置
        └── services/
            ├── parser.py   # 文档解析
            ├── embedding.py # 向量化
            ├── vector.py   # 向量存储
            └── rag.py     # RAG 服务
```

---

## 🛠️ 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| Web UI | Streamlit | 快速原型 |
| 向量数据库 | Qdrant | 轻量级向量存储 |
| Embedding | BGE-large-zh | 中文向量化模型 |
| 文档解析 | PyMuPDF | PDF 处理 |
| LLM | GLM-5 (待接入) | 大语言模型 |

---

## 📊 里程碑

| 阶段 | 时间 | 目标 |
|------|------|------|
| MVP Demo | 2026-03 | 文档解析 + 对话 |
| MVP Pro | Month 3 | 完整 RAG + 图谱 |
| Pro | Month 6 | 个人 AI 伴侣 |
| Enterprise | Month 9 | 企业知识库 |

---

## 💡 核心差异化

| 竞品 | 定位 | 本产品差异 |
|------|------|------------|
| Notion | All-in-One | 知识图谱 + AI 伴侣 |
| Zotero | 学术文献 | AI 辅助 + 记忆 |
| Obsidian | 双链笔记 | 多端 + AI 原生 |
| ChatGPT | AI 对话 | 个人知识库 + 持久记忆 |

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

*让每个人都拥有自己的"知识图书馆"和"AI 学习伴侣"*
