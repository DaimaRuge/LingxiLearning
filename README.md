# 灵犀智读 - 个人终身学习数字读书系统

> 🧠 首款基于大模型 Agent 的个人终身学习数字伴侣

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-green.svg)]()
[![AI](https://img.shields.io/badge/AI-Agent-orange.svg)]()

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

### 核心特性

- 📚 **知识图谱** - Connected Papers 风格的可视化知识关联
- 🤖 **AI 伴侣** - 像"夫子"一样的个人学习伙伴
- 🔍 **智能索引** - 多格式文档自动解析与检索
- 📈 **成长追踪** - 学习轨迹可视化与记忆进化
- ✍️ **创作辅助** - AI 赋能的内容创作

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

### 核心技术栈

| 层级 | 技术 |
|------|------|
| 前端 | React, TypeScript, D3.js |
| 后端 | Python, FastAPI, LangChain |
| 数据库 | PostgreSQL, Neo4j, Milvus, Redis, MinIO |
| AI | GLM-5, BGE, PaddleOCR, Whisper |

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
pip install -r requirements.txt

# 运行后端
cd server && uvicorn main:app --reload

# 运行前端
cd web && npm install && npm run dev
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
