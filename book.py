from flask import Flask, request, redirect, url_for, render_template
import os
import re
import chardet

app = Flask(__name__)

# 存储章节的全局变量
chapters = []
# 设置上传文件的路径
uploaded_file_path = os.path.join('uploads', 'uploaded_novel.txt')

@app.route('/')
def index():
    # 检查文件是否存在
    if os.path.exists(uploaded_file_path):
        # 如果文件存在，直接加载内容
        load_chapters_from_file()
        return redirect(url_for('chapter', chapter=1))
    else:
        # 如果文件不存在，显示上传页面
        return render_template('index.html')

def load_chapters_from_file():
    global chapters
    with open(uploaded_file_path, 'rb') as f:
        raw_data = f.read(50000)  # 读取前 50,000 字节来判断编码
        detected_encoding = chardet.detect(raw_data)['encoding']

    try:
        with open(uploaded_file_path, 'r', encoding=detected_encoding) as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            # 如果用检测到的编码读取失败，尝试使用 utf-8
            with open(uploaded_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            # 如果 utf-8 也读取失败，用 'ignore' 错误处理器
            with open(uploaded_file_path, 'r', encoding=detected_encoding, errors='ignore') as f:
                content = f.read()

    chapter_parts = re.split(r'(\n第[一二三四五六七八九十百千万1234567890]+[章节].*\n)', content)
    preface = chapter_parts.pop(0) if chapter_parts and chapter_parts[0].strip() != '' else '无前言'
    chapters = [('前言', preface)] + [(chapter_parts[i].strip(), chapter_parts[i+1]) for i in range(0, len(chapter_parts), 2) if i+1 < len(chapter_parts)]


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file.save(uploaded_file_path)
        load_chapters_from_file()
        return redirect(url_for('chapter', chapter=1))
    return redirect(url_for('index'))

@app.route('/<int:chapter>')
def chapter(chapter):
    if 0 <= chapter - 1 < len(chapters):
        chapter_title, chapter_content = chapters[chapter - 1]
        return render_template('chapter.html', title=chapter_title, content=chapter_content, next_chapter=chapter + 1, total_chapters=len(chapters))
    return '章节不存在'

if __name__ == '__main__':
    app.run(debug=True)
