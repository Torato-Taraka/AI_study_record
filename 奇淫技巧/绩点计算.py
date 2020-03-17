# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:33:54 2020

@author: 10541
"""

f = open('jidian.txt','r').readlines()
print(f)

score = 0.00
point = 0.00

for i in range(len(f)):
    line = f[i].strip()
    line = line.split(' ')
    #print(line)
    score = score + float(line[0]) * float(line[1])
    point = point + float(line[0])

score = score / point

print(score)
