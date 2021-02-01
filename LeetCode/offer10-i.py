# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:35:17 2021

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：1

示例 2：

输入：n = 5
输出：5
 

提示：

0 <= n <= 100

class Solution:
    def fib(self, n: int) -> int:

@author: qzh
"""

"""
第一种方法是无记忆替换，目标始终只有当前的前两个数字，那么为了最大程度节省空间，就反复
替换就可以了，而且，不可避免要计算n前面所有的数，所以时间上来说应该没法优化了
还有一种方法是递归，但是显然当递归的层数到了一定程度的时候会超时
所以基于递归有更优的方法，记忆式递归，这里没有写出来，就加个类变量就行，记录一下
"""

class Solution:
    def fib(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, (a + b) % 1000000007
        return a
    
    def fib2(self, n):
        if n <= 1:
            return n
        return (self.fib2(n-1) + self.fib2(n-2)) % 1000000007
    
solution = Solution()
print(solution.fib(3))
print(solution.fib2(2))
        