# 几种实现方式
## 方式一 使用[pyhtml2pdf](https://pypi.org/project/pyhtml2pdf/#description)
- 安装依赖 `pip install -r requirements.txt`
- 直接运行 pyhtml2pdf-demo.py
- 底层原理是调用了 Selenium，可以直接看 site-packages下的源码

## 方式二 使用[pdfkit](https://github.com/JazzCore/python-pdfkit)
- 安装依赖 `pip install -r requirements.txt`
- macOS `brew install homebrew/cask/wkhtmltopdf`
- 直接运行 pdfkit-demo.py
- 底层原理是调用了 wkhtml2

