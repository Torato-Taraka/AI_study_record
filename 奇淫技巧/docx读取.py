# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:17:37 2020

@author: 10541
"""

import docx

path = "党史作业 李梓铭.docx"

file = docx.Document(path)

for p in file.paragraphs:
    print(p.text)