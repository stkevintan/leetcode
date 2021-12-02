#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right
# @lc code=start


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # return self.dfs(preorder, inorder)
        return self.stack(preorder, inorder)
    
    def dfs(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        leftSize = inorder.index(preorder[0])
        if leftSize > 0:
            root.left = self.buildTree(
                preorder[1: leftSize + 1], inorder[0: leftSize])
        if leftSize + 1 < len(preorder):
            root.right = self.buildTree(
                preorder[leftSize + 1:], inorder[leftSize + 1:])
        return root
    
    def stack(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        stk: List[TreeNode] = []
        rt = None
        index = 0
        for i in range(len(preorder)):
            if i == 0:
                rt = TreeNode(preorder[i])
                stk.append(rt)
                continue
            if  stk[-1].val != inorder[index]:
                node = TreeNode(preorder[i])
                stk[-1].left = node
                stk.append(node)
            else:
                parent = None 
                while stk and stk[-1].val == inorder[index]:
                    parent = stk.pop()
                    index += 1
                parent.right = TreeNode(preorder[i])
                stk.append(parent.right)
        return rt


# @lc code=end
