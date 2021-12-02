#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right
# @lc code=start


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        prev, cur = None, root
        first, last = None, None
        while cur:
            if cur.left:
                pred = cur.left
                while pred.right and pred.right != cur:
                    pred = pred.right
                if pred.right is None:
                    pred.right = cur
                    cur = cur.left
                    continue
                pred.right = None
            if prev and prev.val > cur.val:
                if not first:
                    first = prev
                last = cur
            prev = cur
            cur = cur.right
        if first:
            first.val, last.val = last.val, first.val
# @lc code=end
