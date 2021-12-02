#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right
# @lc code=start
# Definition for a binary tree node.
# 中序遍历是严格递增的
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.preVal = None
        return self.travel(root)
    
    def travel(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if not self.travel(root.left):
            return False
        if  self.preVal is None or self.preVal < root.val:
            self.preVal = root.val
        else:
            return False
        return self.travel(root.right)
# @lc code=end

