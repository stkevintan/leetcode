#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right
# @lc code=start
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res: List[int] = []
        dummyRoot = TreeNode(-1, root)
        cur = dummyRoot 
        while cur:
            # here is the preorder slot
            if cur.left:
                # find the inorder predecessor  of cur
                pred = cur.left
                while pred.right and pred.right != cur:
                    pred = pred.right
                # predecessor  found:
                if pred.right is None:
                    # connect the predecessor's right child to cur
                    pred.right = cur
                    cur = cur.left
                    continue
                # pred.right is connected before, recover it to None
                pred.right = None
                self.reversedExtend(res, cur.left)
            # here is the inorder slot
            cur = cur.right
        return res
    
    def reversedExtend(self, res: List[int], node: TreeNode):
        tmp = []
        while node:
            tmp.append(node.val)
            node = node.right
        res.extend(reversed(tmp))

# @lc code=end

