# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 09:13:47 2021

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示：

2 <= n <= 58

class Solution:
    def cuttingRope(self, n: int) -> int:

@author: qzh
"""

"""
本题有两种做法
一种是DP，长为n的绳子最多能分为n段，基于此，分成k-1段最短需要k-1长度的绳子
然后从k-1到n就是n-1段绳子的总长的范围，那么最后一段绳子的长度就是1~n-k+1
求k-1段乘以最后一段的长度中的最大值就可以了
时间复杂度O(n^3)，空间复杂度O(n^2)
并不是非常优
第二种做法是，数学法，n分成若干个3的乘积时最大，或者是3*3*……*3*2(*2)最大
这种做法时间复杂度和空间复杂度均为O(1)
"""

class Solution:
    def cuttingRope(self, n):
        a = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            a[1][i] = i
        for i in range(2, n + 1):
            for j in range(i, n + 1):
                a[i][j] = max(a[i - 1][j - k] * k for k in range (1, j - i + 2))
        return max(a[i][n] for i in range(2, n + 1))
    
    def cuttingRope2(self, n):
        if n == 2: return 1
        if n == 3: return 2
        if n % 3 == 1:
            return (3 ** ((n - 4) // 3)) * 4
        elif n % 3 == 0:
            return 3 ** (n // 3)
        else:
            return (3 ** ((n - 2) // 3)) * 2
                        
solution = Solution()
print(solution.cuttingRope(1000))
print(solution.cuttingRope2(2))