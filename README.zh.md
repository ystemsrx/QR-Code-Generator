[English](README.md)

# DALL-E 3背景二维码生成器

## 概述
这个基于Python的应用程序允许用户生成带有独特背景的自定义二维码，背景由DALL-E 3创造。它具有Tkinter构建的图形用户界面，提供URL输入、二维码定制和AI生成背景的选项。

## 特点
- **自定义二维码生成：** 输入URL以生成其二维码。
- **AI生成背景：** 使用DALL-E 3为二维码创建独特背景。
- **定制选项：** 选择背景和二维码颜色，添加标志，并选择语言偏好。
- **语言支持：** 切换英文和简体中文界面。

## 系统要求
- Python 3
- Tkinter
- PIL (Python图像库)
- `qrcode` Python库
- `openai` Python库
- `requests` Python库

## 安装
1. 确保您的系统上安装了Python 3。
2. 安装所需库：`pip install pillow qrcode openai requests`。
3. 将您的OpenAI API密钥设置为环境变量。您可以通过将以下行添加到您的环境变量中来实现：`export OPENAI_API_KEY='your_api_key'`。将`'your_api_key'`替换为您的实际OpenAI API密钥。

## 使用方法
运行脚本`QR Code Generator with DALLE3.py`以打开GUI。按照屏幕上的指示创建您的自定义二维码。


