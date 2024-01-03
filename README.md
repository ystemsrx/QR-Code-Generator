[中文版](README.zh.md)

# QR Code Generator with DALL-E 3 Background

## Overview
This Python-based application allows users to generate custom QR codes with unique backgrounds created using DALL-E 3. It features a GUI built with Tkinter, offering options for URL input, QR code customization, and AI-generated backgrounds.

## Features
- **Custom QR Code Generation:** Input a URL to generate its QR code.
- **AI-Generated Backgrounds:** Utilize DALL-E 3 to create unique backgrounds for QR codes.
- **Customization Options:** Choose background and QR code colors, add logos, and select language preferences.
- **Language Support:** Switch between English and Simplified Chinese interface.

## Requirements
- Python 3
- Tkinter
- PIL (Python Imaging Library)
- `qrcode` Python library
- `openai` Python library
- `requests` Python library

## Installation
1. Ensure Python 3 is installed on your system.
2. Install required libraries: `pip install pillow qrcode openai requests`.
3. Set your OpenAI API key as an environment variable. You can do this by adding the following line to your environment variables: `export OPENAI_API_KEY='your_api_key'`. Replace `'your_api_key'` with your actual OpenAI API key.

## Usage
Run the script `QR Code Generator with DALLE3.py` to open the GUI. Follow the on-screen instructions to create your custom QR code.

