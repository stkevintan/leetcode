#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None
# @lc code=start

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = self.checkLoop(head)
        if not slow:
            return None
        # find the cycle entry
        while head != slow:
            head = head.next
            slow = slow.next
        return head 

    def checkLoop(self, head: ListNode) -> ListNode:
        fast = slow = head
        # at first fast is equals slow
        # we cannot use: while fast != slow:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow 
        return None 

# @lc code=end

