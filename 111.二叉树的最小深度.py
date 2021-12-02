#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.right and root.left:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        if root.right:
            return 1 + self.minDepth(root.right)
        if root.left:
            return 1 + self.minDepth(root.left)
        return 1
# @lc code=end

