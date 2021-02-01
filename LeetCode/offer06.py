# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:17:10 2021

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 
限制：

0 <= 链表长度 <= 10000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:

@author: qzh
"""

"""
递归遍历
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def reversePrint(self, head):
        result = []
        while head != None:
            result.insert(0, head.val)
            head = head.next
        return result
    
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
head.next = node1
node1.next = node2
solution = Solution()
print(solution.reversePrint(head))
