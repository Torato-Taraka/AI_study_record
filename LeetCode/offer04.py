# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:49:26 2021

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下
递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是
否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。

给定 target = 20，返回 false。 

限制：

0 <= n <= 1000

0 <= m <= 1000

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

@author: qzh
"""

"""
一种方法是将矩阵一维化，然后可以以集合的方式，直接查找索引
第二种方法是考虑规律，从左到右变大，从上到下变大，那么考虑二叉搜索的思想，先找一个中间数
也就是左下角或者右上角的那两个数
以右上角为例，比他大就找下面的，也就是i++
比他小就找左边的，也就是j--
"""

class Solution:
    def findNumberIn2DArray(self, matrix, target) -> bool:
        matrix = [i for j in matrix for i in j]
        if target in matrix:
            return True
        return False
    
    def findNumberIn2DArray1(self, matrix, target) -> bool:
        i = 0
        j = len(matrix[0]) - 1
        if (j < 0):
            return False
        while i < len(matrix) and j >= 0:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                return True
        return False
                
        
a = [[1,   4,  7, 11, 15],
     [2,   5,  8, 12, 19],
     [3,   6,  9, 16, 22],
     [10, 13, 14, 17, 24],
     [18, 21, 23, 26, 30]]
b = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
solution = Solution()
print(solution.findNumberIn2DArray(a, 20))
print(solution.findNumberIn2DArray1(b, 5))
