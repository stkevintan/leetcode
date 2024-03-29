#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
from typing import Any


class ListNode:
    def __init__(self, val=0, next: Any = None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        Root = Cur = ListNode()
        while l1 or l2:
            if l1 is None or (l2 is not None and l1.val > l2.val):
                l1, l2 = l2, l1
            Cur.next = l1
            Cur, l1 = l1, l1.next
        return Root.next
                

# @lc code=end

