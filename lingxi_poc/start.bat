@echo off
chcp 65001 >nul
echo ========================================
echo   灵犀智读 - MVP Demo 启动脚本
echo ========================================
echo.

:: 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到 Python，请先安装 Python 3.10+
    pause
    exit /b 1
)

echo [1/4] 检查依赖...
pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo        安装 streamlit...
    pip install streamlit -q
)

:: 安装依赖
echo [2/4] 安装项目依赖...
pip install -r requirements.txt -q

:: 检查 Qdrant
echo [3/4] 检查 Qdrant 向量数据库...
docker ps | findstr qdrant >nul
if errorlevel 1 (
    echo        提示: Qdrant 未运行，请执行: docker run -d -p 6333:6333 qdrant/qdrant
)

:: 启动
echo [4/4] 启动 Streamlit...
echo.
echo ========================================
echo   启动成功！
echo   访问: http://localhost:8501
echo ========================================
echo.

streamlit run app.py --server.port 8501

pause
