# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:18:00 2021

找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

限制：

2 <= n <= 100000

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:

@author: qzh
"""

"""
一种方法是，字典索引
一种方法是，初始化hash数组为长度n，然后把对应数字放到对应位置
另一种方法是，不需要hash数组，直接进行置换操作，与对应位置的数进行互换，如果
对应位置有相同数字，则说明重复了
"""

class Solution:
    def findRepeatNumber(self, nums):
        a = {}
        for i in nums:
            if i in a:
                return i
            a[i] = 1
            
    def findRepeatNumber1(self, nums):
        a = [0]*len(nums)
        for i in nums:
            if a[i] != 0:
                return i
            a[i] = 1;
    
    def findRepeatNumber2(self, nums):
        for i in range(len(nums)):
            if nums[i] == i:
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            t = nums[i]
            nums[i] = nums[t]
            nums[t] = t
        
a = [0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
solution = Solution()
print(solution.findRepeatNumber(a))
print(solution.findRepeatNumber1(a))
print(solution.findRepeatNumber2(a))




