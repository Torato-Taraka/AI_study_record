# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:08:40 2020

@author: 10541
"""

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

path = "test.pdf"

# 用文件对象来创建一个pdf文档分析器
praser = PDFParser(open(path, 'rb'))
# 创建一个PDF文档
doc = PDFDocument()
# 连接分析器 与文档对象
praser.set_document(doc)
doc.set_parser(praser)

# 提供初始化密码
# 如果没有密码 就创建一个空的字符串
doc.initialize()

# 检测文档是否提供txt转换，不提供就忽略
if not doc.is_extractable:
    raise PDFTextExtractionNotAllowed
else:
    # 创建PDf 资源管理器 来管理共享资源
    rsrcmgr = PDFResourceManager()
    # 创建一个PDF设备对象
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    # 创建一个PDF解释器对象
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # 循环遍历列表，每次处理一个page的内容
    for page in doc.get_pages():
        interpreter.process_page(page)                        
        # 接受该页面的LTPage对象
        layout = device.get_result()
        # 这里layout是一个LTPage对象，里面存放着这个 page 解析出的各种对象
        # 包括 LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等                            
        for x in layout:
            if isinstance(x, LTTextBox):
                print(x.get_text().strip())