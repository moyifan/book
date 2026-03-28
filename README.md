# Flask Novel Reader

## 项目简介

这是一个基于 Flask 框架开发的小说阅读器，旨在提供一个简洁、高效的在线阅读体验。它支持用户上传 `.txt` 格式的小说文件，并能自动识别文件编码、智能解析章节。界面通过集成 Bootstrap 5 实现了响应式设计，确保在不同设备上都能有良好的显示效果。

## 功能特点

- **文件上传**：用户可以轻松上传本地的 `.txt` 格式小说文件。
- **自动编码检测**：利用 `chardet` 库自动检测上传文件的编码，避免乱码问题。
- **智能章节解析**：通过正则表达式智能识别小说章节，自动将小说内容分割成独立的章节。
- **响应式界面**：集成 Bootstrap 5，提供美观且适应各种屏幕尺寸的用户界面。
- **章节导航**：方便地在前言、各章节之间进行切换。
- **章节管理**：支持删除当前书籍，方便重新上传。
- **兼容阅读模式脚本**：章节内容输出时，将每段内容包裹在 `<p>` 标签中，确保与浏览器阅读模式插件（如油猴脚本 MyNovelReader）的良好兼容性。

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/moyifan/book.git
cd book
```

### 2. 创建虚拟环境并激活

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. 安装依赖

```bash
pip install Flask chardet
```

### 4. 运行应用

```bash
python book.py
```

应用将在 `http://127.0.0.1:5000` 启动。

## 使用说明

1. **上传小说**：访问应用首页，通过上传表单选择你的 `.txt` 格式小说文件并上传。
2. **开始阅读**：上传成功后，应用会自动跳转到第一章，你可以在章节页面进行阅读。
3. **章节切换**：使用页面底部的“上一章”和“下一章”按钮进行章节导航。
4. **删除书籍**：在章节页面底部点击“删除当前书籍”按钮，即可清除当前书籍数据并返回首页。

## 预览截图

![上传页面截图](placeholder_upload.png)
![章节阅读页面截图](placeholder_chapter.png)

# Flask Novel Reader (English Version)

## Project Introduction

This is a novel reader developed with the Flask framework, aiming to provide a simple and efficient online reading experience. It supports users uploading `.txt` format novel files, automatically detects file encoding, and intelligently parses chapters. The interface integrates Bootstrap 5 for a responsive design, ensuring a good display effect on various devices.

## Features

- **File Upload**: Users can easily upload local `.txt` format novel files.
- **Automatic Encoding Detection**: Utilizes the `chardet` library to automatically detect the encoding of uploaded files, preventing garbled text issues.
- **Smart Chapter Parsing**: Intelligently identifies novel chapters using regular expressions, automatically splitting the novel content into independent chapters.
- **Responsive Interface**: Integrates Bootstrap 5 to provide a beautiful and adaptable user interface for various screen sizes.
- **Chapter Navigation**: Easily switch between the preface and different chapters.
- **Chapter Management**: Supports deleting the current book for easy re-uploading.
- **Compatibility with Reading Mode Scripts**: Chapter content is outputted with each paragraph wrapped in `<p>` tags, ensuring good compatibility with browser reading mode extensions (e.g., Tampermonkey script MyNovelReader).

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/moyifan/book.git
cd book
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install Flask chardet
```

### 4. Run the Application

```bash
python book.py
```

The application will start at `http://127.0.0.1:5000`.

## Usage Instructions

1. **Upload Novel**: Visit the application homepage, select your `.txt` format novel file through the upload form, and upload it.
2. **Start Reading**: After successful upload, the application will automatically redirect to the first chapter, where you can start reading.
3. **Chapter Navigation**: Use the "Previous Chapter" and "Next Chapter" buttons at the bottom of the page to navigate between chapters.
4. **Delete Book**: Click the "Delete current book" button at the bottom of the chapter page to clear the current book data and return to the homepage.

## Preview Screenshots

![Upload Page Screenshot](placeholder_upload.png)
![Chapter Reading Page Screenshot](placeholder_chapter.png)
