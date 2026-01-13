@echo off

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未找到Python。请先安装Python。
    echo 你可以从 https://www.python.org/downloads/ 下载并安装Python
    pause
    exit /b 1
)

REM 运行转换脚本
python md_to_pdf_converter.py

REM 等待用户按下任意键后退出
pause