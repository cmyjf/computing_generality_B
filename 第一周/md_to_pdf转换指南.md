# Markdown 转 PDF 转换指南

本指南提供了多种将 Markdown (.md) 文件转换为 PDF 文件的方法，特别针对当前目录下的 `assignment1.md` 文件。

## 方法一：使用提供的 Python 脚本

我已经为你创建了一个名为 `md_to_pdf_converter.py` 的 Python 脚本，它可以帮助你将 Markdown 文件转换为 PDF。

### 使用步骤：

1. **确保已安装 Python**
   - 如果你不确定是否安装了 Python，可以在命令提示符中输入 `python --version` 来检查
   - 如果未安装，请从官网下载并安装：https://www.python.org/downloads/

2. **运行转换脚本**
   - 在文件资源管理器中打开当前目录
   - 在地址栏输入 `cmd` 并按回车，打开命令提示符
   - 输入以下命令并按回车：
     ```
     python md_to_pdf_converter.py
     ```
   - 脚本会自动尝试转换当前目录下的 `assignment1.md` 文件

3. **可能的依赖安装**
   - 脚本会尝试自动安装所需的 Python 库（`pdfkit` 和 `markdown`）
   - 但是，你需要手动安装 `wkhtmltopdf` 工具，这是一个必要的依赖项：
     - 从官方网站下载：https://wkhtmltopdf.org/downloads.html
     - 选择适合你操作系统的版本进行安装
     - 安装完成后，确保将 `wkhtmltopdf` 添加到系统 PATH 环境变量中

## 方法二：使用 Typora 软件（推荐）

根据作业文档中提到的，你可以使用 Typora 软件来编辑和转换 Markdown 文件：

1. **下载并安装 Typora**
   - 访问官方网站：https://typoraio.cn
   - 下载适合你操作系统的版本并安装

2. **转换文件**
   - 使用 Typora 打开 `assignment1.md` 文件
   - 点击菜单栏的 "文件" -> "导出" -> "PDF"
   - 选择保存位置，点击 "保存" 完成转换

## 方法三：使用在线转换工具

如果上述方法都不适合你，你可以使用在线 Markdown 转 PDF 工具：

- https://md2pdf.netlify.app/
- https://markdown2pdf.com/
- https://www.convertio.co/zh/md-pdf/

使用步骤通常是：
1. 上传你的 `assignment1.md` 文件
2. 点击转换按钮
3. 下载生成的 PDF 文件

## 方法四：使用 VS Code 插件

如果你使用 Visual Studio Code 编辑器，可以安装 Markdown PDF 插件：

1. 在 VS Code 中打开扩展面板（Ctrl+Shift+X）
2. 搜索并安装 "Markdown PDF"
3. 使用 VS Code 打开 `assignment1.md` 文件
4. 右键点击编辑器，选择 "Markdown PDF: Export (pdf)"

## 注意事项

- 转换后的 PDF 文件可能需要根据你的需求进行格式调整
- 确保转换后的 PDF 文件保留了原始 Markdown 文件中的所有内容，包括表格、代码块等
- 根据作业要求，请将转换后的 PDF 文件作为主要提交文件，并将原始的 `.md` 或 `.docx` 文件作为附件上传

如果在转换过程中遇到任何问题，请尝试使用不同的方法或参考相关工具的官方文档。