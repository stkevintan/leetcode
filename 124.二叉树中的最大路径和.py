#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right
# @lc code=start

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float('inf')
        self.travel(root)
        return self.ans

    def travel(self, root: TreeNode) -> int:
        val = []
        if root.left:
            val.append(self.travel(root.left))
        if root.right:
            val.append(self.travel(root.right))
        if val:
            self.ans = max(self.ans, root.val, root.val + max(val), root.val + sum(val))
            return max(root.val, root.val + max(val))
        else:
            self.ans = max(self.ans, root.val)
            return root.val


        
# @lc code=end

