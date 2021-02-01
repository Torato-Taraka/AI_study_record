# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:38:43 2021

@author: qzh
"""

"""
//判断类型
print(type(1) == int)

//截片
print('ssssss1'[:-1])

//初始化二维数组
a = [[0] * m for _ in range(n)]


"""
import numpy as np
m = 38
n = 15
a = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        a[i][j] = i % 10 + i // 10 + j % 10 + j // 10
    print(a[i])

for i in np.unique(a):
	print(int(i), ' ', np.sum(a == i))