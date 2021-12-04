#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

from collections import deque
from typing import Deque, Dict, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        return self.bfs(root)
    
    def bfs(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        Q: Deque[TreeNode] = deque([root])
        ans = []
        while Q:
            n = len(Q)
            for i in range(n):
                top = Q.popleft()
                if top.left:
                    Q.append(top.left)
                if top.right:
                    Q.append(top.right)
                if i == n - 1:
                    ans.append(top.val)
        return ans



    # apply the strategy of leetcode 117 to travel the tree by layers
    def rightSideView2(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        nextRec: Dict[TreeNode, TreeNode] = {}
        ans = []
        cur = root
        first, prev = None, None
        while cur:
            if cur.left:
                if prev:
                    nextRec[prev] = cur.left
                prev = cur.left
                if not first:
                    first = cur.left
            if cur.right:
                if prev: 
                    nextRec[prev] = cur.right
                prev = cur.right
                if not first:
                    first = cur.right
            
            next = nextRec.get(cur, None)
            if next:
                cur = next
            # right most
            else:
                ans.append(cur.val)
                cur = first
                first, prev = None, None
        return ans


            


# @lc code=end

