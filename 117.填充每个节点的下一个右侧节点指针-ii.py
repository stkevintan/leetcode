#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
# @lc code=start
"""
# Definition for a Node.

"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        return self.reuseNext(root)

    def bfs(self, root: 'Node') -> 'Node':
        if not root:
            return None
        Q = deque([(root, 0)])
        prevNode: 'Node' = None
        prevDep: int = 0
        while Q:
            (node, dep) = Q.popleft()
            if dep > prevDep:
                prevNode = None
                prevDep = dep
            if prevNode:
                prevNode.next = node
            prevNode = node
            if node.left:
                Q.append((node.left, dep + 1))
            if node.right:
                Q.append((node.right, dep + 1))
        return root 

    def reuseNext(self, root: 'Node') -> 'Node':
        start = root
        
        while start:
            cur = start
            nextStart: 'None' = None
            prevNode: 'Node' = None
            while cur:
                if cur.left:
                    if prevNode:
                        prevNode.next = cur.left
                    prevNode = cur.left
                    if not nextStart:
                        nextStart = prevNode
                if cur.right:
                    if prevNode:
                        prevNode.next = cur.right
                    prevNode = cur.right
                    if not nextStart:
                        nextStart = prevNode
                cur = cur.next
            start = nextStart
        return root
        

            


        
# @lc code=end

