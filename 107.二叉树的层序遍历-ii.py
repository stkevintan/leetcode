#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

from typing import Dict, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

# @lc code=start
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.maxLevel = 0
        self.levelMap: Dict[int, List[int]] = {}
        self.dfs(root, 0);
        ans = []
        for i in range(self.maxLevel - 1, -1, -1):
            ans.append(self.levelMap[i])
        return ans

    def dfs(self, root: TreeNode, level: int) -> None:
        if root is None:
            self.maxLevel = max(self.maxLevel, level)
            return 
        if level in self.levelMap:
            self.levelMap[level].append(root.val)
        else:
            self.levelMap[level] = [root.val]
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)
    
    

# @lc code=end

