# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:57:26 2021

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2

示例 2：

输入：n = 7
输出：21

示例 3：

输入：n = 0
输出：1

提示：

0 <= n <= 100

class Solution:
    def numWays(self, n: int) -> int:

@author: qzh
"""

class Solution:
    def numWays(self, n):
        a, b = 1, 2
        for _ in range(n-1):
            a, b = b, (a + b) % 1000000007
        return a
    
solution = Solution()
print(solution.numWays(1))