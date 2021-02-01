# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:09:27 2021

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：

0 <= s 的长度 <= 10000

class Solution:
    def replaceSpace(self, s: str) -> str:

@author: qzh
"""

"""
遍历
"""

class Solution:
    def replaceSpace(self, s) -> str:
        result = ''
        for i in s:
            if i == ' ':
                result += '%20'
            else:
                result += i
        return result
        
a = "We are happy."
solution = Solution()
print(solution.replaceSpace(a))