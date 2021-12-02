#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

# @lc code=start

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.ans = True  
        self.dfs(root)
        return self.ans
    
    def dfs(self, root: TreeNode) -> int:
        if self.ans == False:
            return -1
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            self.ans = False
            return -1
        return 1 + max(left, right)
        
        
# @lc code=end

