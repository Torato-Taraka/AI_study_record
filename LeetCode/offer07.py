# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:33:07 2021

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000

Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

@author: qzh
"""

"""
此题于我意义重大
二叉树的遍历方法得了然于胸，递归的非递归的都得弄懂才行
第一种方法就是递归
第二种方法是非递归
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def buildTree(self, preorder, inorder):
        if preorder == [] or inorder == []:
            return None
        root = TreeNode(preorder[0])
        ir = inorder.index(preorder[0])
        if ir != 0:
            root.left = self.buildTree(preorder[1: ir + 1], inorder[0: ir])
        if ir + 1 != len(inorder):
            root.right = self.buildTree(preorder[ir + 1: len(preorder)], inorder[ir + 1: len(inorder)])
        return root
    
    def buildTree2(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        stack = []
        p_p = 0
        p_i = 0
        current = root
        while p_p < len(preorder):
            while p_p < len(preorder) and preorder[p_p] != inorder[p_i]:
                p_p += 1
                stack.append(current)
                if p_p <len(preorder):
                    current.left = TreeNode(preorder[p_p])
                    current = current.left
                
            p_i += 1
            while stack != [] and inorder[p_i] == stack[-1].val:
                current = stack.pop(-1)
                p_i += 1
            
            p_p += 1
            
            if p_p < len(preorder):
                current.right = TreeNode(preorder[p_p])
                current = current.right
        return root
      
def print_tree(root):
    global tree
    tree += str(root.val)
    if root.left != None:
        tree += '('
        print_tree(root.left)
    if root.right != None:
        if root.left == None:
            tree += '('
        tree += ','
        print_tree(root.right)
        tree += ')'
    
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution = Solution()
tree = ''  
print_tree(solution.buildTree(preorder, inorder))
print(tree)
tree = ''
print_tree(solution.buildTree2(preorder, inorder))
print(tree)

preorder = [1,2,3]
inorder = [2,3,1]

solution = Solution()
tree = ''  
print_tree(solution.buildTree(preorder, inorder))
print(tree)
tree = ''
print_tree(solution.buildTree2(preorder, inorder))
print(tree)