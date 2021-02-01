# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:34:38 2021

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的
数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一
个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1

示例 2：

输入：[2,2,2,0,1]
输出：0

class Solution:
    def minArray(self, numbers: List[int]) -> int:

@author: qzh
"""

"""
很简单的方法就是直接找最小的
还有一种方法，较为复杂一点，就是用二分法做，但是当存在很多一样的数字
比如，[2, 2, 2, 0, 2] 或者 [2, 0, 2, 2, 2] 这个样子的时候，就比较麻烦了
"""

class Solution:
    def minArray(self, numbers):
        return min(numbers)
    
    def minArray2(self, numbers):
        l, r = 0, len(numbers) - 1
        while l < r:
            mid = int((l - r) / 2)
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                return min(numbers[l:r])
        return numbers[l]

solution = Solution()
print(solution.minArray([3,4,5,1,2]))