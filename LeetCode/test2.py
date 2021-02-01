# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:44:20 2021

@author: qzh
"""

class Solution:
    def getLocation(self , n , q , req ):
        result = []
        for i in req:
            if i == n:
                result.append(i)
            else:
                if i % 2 == 1:
                    result.append((i + 1) // 2)
                else:
                    result.append(n - (i // 2))
        return result
    
solution = Solution()
print(solution.getLocation(1, 9, [1]))
print(solution.getLocation(2, 9, [1,2]))
print(solution.getLocation(3, 9, [1,2,3]))
print(solution.getLocation(4, 9, [1,2,3,4]))
print(solution.getLocation(5, 9, [1,2,3,4,5]))
print(solution.getLocation(6, 9, [1,2,3,4,5,6]))
print(solution.getLocation(7, 9, [1,2,3,4,5,6,7]))
print(solution.getLocation(8, 9, [1,2,3,4,5,6,7,8]))
print(solution.getLocation(5, 3, [1,3,4]))
print(solution.getLocation(1, 9, [1]))