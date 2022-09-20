#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' | None = None, random: 'Node' | None  = None):
        self.val = int(x)
        self.next = next
        self.random = random

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        copy = Node(0)
        p, q = head, copy
        while p:
            q.next = Node(p.val)
            q = q.next
            q.random = p.random
            p.random = q
            p = p.next
        q = copy.next
        while q:
            q.random = q.random.random if q.random else None
            q = q.next
        return copy.next

        
        

        
# @lc code=end

