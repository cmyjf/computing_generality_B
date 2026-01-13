import os
import subprocess
import sys

# 检查是否安装了必要的库
try:
    import pdfkit
except ImportError:
    print("正在安装必要的库...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pdfkit'])
        import pdfkit
    except Exception as e:
        print(f"安装pdfkit失败: {e}")
        print("\n请手动安装wkhtmltopdf和pdfkit库:")
        print("1. 下载并安装wkhtmltopdf: https://wkhtmltopdf.org/downloads.html")
        print("2. 安装pdfkit: pip install pdfkit")
        sys.exit(1)

try:
    import markdown
except ImportError:
    print("正在安装markdown库...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'markdown'])
        import markdown
    except Exception as e:
        print(f"安装markdown失败: {e}")
        print("请手动安装: pip install markdown")
        sys.exit(1)

def md_to_pdf(input_file, output_file=None):
    """将markdown文件转换为PDF文件"""
    # 如果未指定输出文件名，则使用输入文件名的基础上修改扩展名
    if output_file is None:
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}.pdf"
    
    try:
        # 读取markdown文件
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # 将markdown转换为HTML
        html_content = markdown.markdown(md_content)
        
        # 保存HTML到临时文件
        temp_html = f"{os.path.splitext(input_file)[0]}_temp.html"
        with open(temp_html, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        try:
            # 尝试使用pdfkit将HTML转换为PDF
            pdfkit.from_file(temp_html, output_file)
            print(f"PDF转换成功！输出文件: {output_file}")
        except OSError as e:
            # 如果wkhtmltopdf未找到，提供下载指引
            if 'No wkhtmltopdf executable found' in str(e):
                print("错误: 未找到wkhtmltopdf可执行文件。")
                print("请下载并安装wkhtmltopdf: https://wkhtmltopdf.org/downloads.html")
                print("安装完成后，确保将wkhtmltopdf添加到系统PATH中，或在pdfkit配置中指定其路径。")
            else:
                print(f"PDF转换失败: {e}")
        finally:
            # 清理临时HTML文件
            if os.path.exists(temp_html):
                os.remove(temp_html)
        
    except Exception as e:
        print(f"处理文件时出错: {e}")

if __name__ == "__main__":
    # 默认转换当前目录下的assignment1.md文件
    default_input = "assignment1.md"
    
    # 检查是否提供了命令行参数
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = default_input
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误: 找不到文件 '{input_file}'")
        sys.exit(1)
    
    # 执行转换
    md_to_pdf(input_file)
    
    # 提供替代方法的提示
    print("\n替代方法：")
    print("1. 使用在线转换工具，如: https://md2pdf.netlify.app/")
    print("2. 使用Typora软件（文档中推荐的）：打开.md文件后，选择'文件'->'导出'->'PDF'")
    print("3. 使用VS Code的Markdown PDF插件")