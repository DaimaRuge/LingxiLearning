"""
灵犀智读 - Streamlit Web UI
MVP Demo 快速演示
"""
import streamlit as st
import sys
import os

# 添加 backend 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from services.parser import DocumentParser
from services.embedding import get_embedding_service
from services.vector import get_vector_store
from services.rag import RAGService

# 页面配置
st.set_page_config(
    page_title="灵犀智读 - MVP Demo",
    page_icon="📚",
    layout="wide"
)

# 标题
st.title("📚 灵犀智读 - 个人终身学习数字伴侣")
st.markdown("*基于大模型 Agent 的智能知识管理系统*")

# 侧边栏
with st.sidebar:
    st.header("功能导航")
    page = st.radio(
        "选择功能",
        ["📖 文档库", "💬 AI 对话", "🗺️ 知识图谱", "📊 个人中心"]
    )
    
    st.divider()
    st.markdown("**系统状态**")
    st.info("🤖 AI: GLM-5 待接入")
    st.info("📦 向量库: Qdrant")

# 文档库页面
if page == "📖 文档库":
    st.header("📖 文档库")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("导入文档")
        uploaded_file = st.file_uploader(
            "拖拽或点击上传",
            type=['pdf', 'txt', 'md'],
            help="支持 PDF、TXT、Markdown 格式"
        )
        
        if uploaded_file:
            st.success(f"已上传: {uploaded_file.name}")
            
            # 保存临时文件
            temp_path = f"temp_{uploaded_file.name}"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # 解析按钮
            if st.button("🔍 解析文档"):
                with st.spinner("正在解析..."):
                    parser = DocumentParser()
                    doc = parser.parse(temp_path)
                    
                    st.session_state['current_doc'] = doc
                    st.session_state['doc_name'] = uploaded_file.name
                    
                    # 清理
                    os.remove(temp_path)
        
        st.divider()
        
        # 文档列表
        st.subheader("📁 文档列表")
        if 'documents' in st.session_state:
            for doc in st.session_state['documents']:
                st.text(f"📄 {doc}")
        else:
            st.session_state['documents'] = []
            st.info("暂无文档，请上传")
    
    with col2:
        if 'current_doc' in st.session_state:
            doc = st.session_state['current_doc']
            st.subheader(f"📄 {st.session_state['doc_name']}")
            
            # 元数据
            col_meta = st.columns(3)
            with col_meta[0]:
                st.metric("字数", len(doc.get('content', '')))
            with col_meta[1]:
                st.metric("段落", len(doc.get('chunks', [])))
            with col_meta[2]:
                st.metric("格式", doc.get('metadata', {}).get('format', 'unknown'))
            
            st.divider()
            
            # 内容预览
            st.subheader("内容预览")
            content = doc.get('content', '')[:2000]
            st.text_area("文档内容", content, height=300, disabled=True, label_visibility="collapsed")
            
            # 分块信息
            if doc.get('chunks'):
                st.subheader("分块预览")
                for i, chunk in enumerate(doc['chunks'][:3]):
                    with st.expander(f"分块 {i+1}"):
                        st.text(chunk[:500])
        else:
            st.info("👆 请先上传并解析文档")

# AI 对话页面
elif page == "💬 AI 对话":
    st.header("💬 AI 对话")
    
    # 初始化 RAG 服务
    try:
        rag = RAGService()
        rag_status = "✅ RAG 服务就绪"
    except Exception as e:
        rag = None
        rag_status = f"❌ RAG 服务异常: {str(e)[:50]}"
    
    st.info(rag_status)
    
    # 对话历史
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    
    # 显示对话历史
    for msg in st.session_state['chat_history']:
        with st.chat_message(msg['role']):
            st.markdown(msg['content'])
    
    # 输入框
    user_input = st.chat_input("输入问题，按 Enter 发送...")
    
    if user_input:
        # 添加用户消息
        st.session_state['chat_history'].append({
            'role': 'user',
            'content': user_input
        })
        
        with st.chat_message('user'):
            st.markdown(user_input)
        
        # AI 回复
        with st.chat_message('assistant'):
            if rag:
                with st.spinner("思考中..."):
                    result = rag.generate_answer(user_input)
                    
                    # 显示回答
                    st.markdown(result['answer'])
                    
                    # 显示引用
                    if result.get('references'):
                        with st.expander("📚 参考资料"):
                            for i, ref in enumerate(result['references'][:3]):
                                st.markdown(f"**[{i+1}]** {ref['payload']['content'][:200]}...")
                    
                    # 保存到历史
                    st.session_state['chat_history'].append({
                        'role': 'assistant',
                        'content': result['answer']
                    })
            else:
                st.error("RAG 服务不可用，请检查 Qdrant 连接")
        
        st.rerun()
    
    # 清空对话
    if st.button("🗑️ 清空对话"):
        st.session_state['chat_history'] = []
        st.rerun()

# 知识图谱页面
elif page == "🗺️ 知识图谱":
    st.header("🗺️ 知识图谱")
    st.info("🚧 知识图谱模块开发中...")
    
    st.markdown("""
    ### 规划中的功能
    
    - 📊 可视化知识网络
    - 🔗 Connected Papers 风格文献关系
    - 🎯 智能文献推荐
    - 🔍 图谱搜索与导航
    """)
    
    # 模拟图谱展示
    st.subheader("预览效果")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("知识节点", "1,234")
    with col2:
        st.metric("关联关系", "5,678")
    with col3:
        st.metric("文档总数", "56")

# 个人中心页面
elif page == "📊 个人中心":
    st.header("📊 个人中心")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("学习统计")
        st.metric("总文档数", "0")
        st.metric("总对话次数", "0")
        st.metric("知识图谱节点", "0")
        
        st.divider()
        
        st.subheader("AI 伴侣状态")
        st.info("🤖 灵犀 - 待初始化")
        st.progress(30, text="学习进度 30%")
    
    with col2:
        st.subheader("最近活动")
        st.info("暂无活动记录")
        
        st.divider()
        
        st.subheader("系统设置")
        st.toggle("Dark Mode")
        st.selectbox("AI 模型", ["GLM-5", "GPT-4", "Claude"])
        st.selectbox("Embedding", ["BGE-large-zh", "M3E"])

# 页脚
st.divider()
st.markdown(
    "📚 灵犀智读 - MVP Demo | "
    "基于 Streamlit + FastAPI + Qdrant + GLM-5 | "
    "© 2026 DaimaRuge"
)
