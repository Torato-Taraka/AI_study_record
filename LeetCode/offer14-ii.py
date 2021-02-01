# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:12:25 2021

和offer14-i的区别在于
2 <= n <= 1000

class Solution:
    def cuttingRope(self, n: int) -> int:

@author: qzh
"""

"""
和上一题的仅有的区别就在于n放大到了1000
这就意味着原本的DP一定会超时
只剩下了数学法
"""

class Solution:
    def cuttingRope(self, n):
        if n == 2: return 1
        if n == 3: return 2
        if n % 3 == 1:
            return (3 ** ((n - 4) // 3)) * 4 % 1000000007
        elif n % 3 == 0:
            return 3 ** (n // 3) % 1000000007
        else:
            return (3 ** ((n - 2) // 3)) * 2 % 1000000007

solution = Solution()
print(solution.cuttingRope(1000))