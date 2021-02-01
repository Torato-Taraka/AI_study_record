# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:43:20 2021

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的
格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐
标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为
3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：

输入：m = 2, n = 3, k = 1
输出：3

示例 2：

输入：m = 3, n = 1, k = 0
输出：1

提示：

1 <= n,m <= 100
0 <= k <= 20

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

@author: qzh
"""

"""
第一种方法，BFS，模拟机器人的路径
第二种方法，DP
可以先打印一下一个和的矩阵，看看规律
import numpy as np
m = 38
n = 15
a = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        a[i][j] = i % 10 + i // 10 + j % 10 + j // 10
    print(a[i])
然后可以发现，第一列和第一行，都是有规律的，如果k比某个数小，那么就停在了这一行（列）
往后都到不了，所以初始化边界，以k为判断
之后状态转移方程为
    a[i][j] = (a[i-1][j] || a[i][j-1]) && sum(i, j) <= k
必须在能从上边或者左边能到的情况下才能考虑本身的大小，不然哪怕本身理论上可以到，但是
不能从周围到也没办法真的到达
"""

class Solution:
    def movingCount(self, m, n, k):
        cnt = 1
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        a = [[0] * n for _ in range(m)]
        sq = [[0, 0]]
        a[0][0] = 1
        f, r = -1, 0
        while f < r :
            f += 1
            for i in range(4):
                x, y = sq[f][0] + d[i][0], sq[f][1] + d[i][1]
                if x >= 0 and x < m and y >= 0 and y < n:
                    if a[x][y] == 0 and x % 10 + x // 10 + y % 10 + y // 10 <= k:
                        a[x][y] = 1
                        r += 1
                        sq.append([x, y])
                        cnt += 1
        return cnt
    
    def movingCount2(self, m, n, k):
        cnt = 0
        a = [[0] * n for _ in range(m)]
        for i in range(m):
            if i % 10 + i // 10 <= k:
                cnt += 1
                a[i][0] = 1
            else:
                break
        for i in range(1, n):
            if i % 10 + i // 10 <= k:
                cnt +=1 
                a[0][i] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if (a[i-1][j] or a[i][j-1]) and i % 10 + i // 10 + j % 10 + j // 10 <= k:
                    a[i][j] = 1
                    cnt += 1
        return cnt
                
        
solution = Solution()
print(solution.movingCount(38, 15, 9))
print(solution.movingCount(3, 2, 1))
print(solution.movingCount(2, 3, 1))
print(solution.movingCount(3, 5, 9))
print(solution.movingCount(3, 1, 0))
print(solution.movingCount(16, 8, 4))
print(solution.movingCount2(38, 15, 9))
print(solution.movingCount2(3, 2, 1))
print(solution.movingCount2(2, 3, 1))
print(solution.movingCount2(3, 5, 9))
print(solution.movingCount2(3, 1, 0))
print(solution.movingCount2(16, 8, 4))