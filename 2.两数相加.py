#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = node = ListNode(0)
        while l1 is not None or l2 is not None or carry > 0:
            val1, l1 = (0, None) if l1 is None else (l1.val, l1.next)
            val2, l2 = (0, None) if l2 is None else (l2.val, l2.next)
            carry, cur = divmod(carry + val1 + val2, 10)
            node.next = ListNode(cur)
            node = node.next

        return head.next

# @lc code=end

