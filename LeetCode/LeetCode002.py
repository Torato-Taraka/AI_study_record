# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:45:24 2019
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        temp = l3
        c = 0
        
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            x = x + y + c
            temp.next = ListNode( x % 10 )
            temp = temp.next
            c = x // 10
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
            
        if (c > 0):
            temp.next = ListNode(1)
        return l3.next

        
l11 = ListNode(2)
l12 = ListNode(4) 
l11.next = l12
l13 = ListNode(3)
l12.next = l13
l21 = ListNode(5)
l22 = ListNode(6)
l21.next = l22
l23 = ListNode(4)
l22.next = l23

solution = Solution()
l3 = solution.addTwoNumbers(l11, l21)
while (l3):
    print(l3.val)
    l3 = l3.next