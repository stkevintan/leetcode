#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None 
        # return self.recursive(head)
        return self.iterate2(head)

    
    def recursive(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        start, end = self.recursive(head.next), head.next 
        head.next, end.next = None, head 
        return start
    
    def iterate(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, None)
        while head:
            next = head.next
            dummy.next, head.next = head, dummy.next
            head = next
        return dummy.next

    def iterate2(self, head: ListNode) -> ListNode:
        tail = head
        while next:= tail.next:
            tail.next, next.next = next.next, head
            head = next
        return head
            
    def iterate3(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        # everytime, we move current node to be the head
        while cur:
            next, cur.next = cur.next, prev
            prev, cur = cur, next
        return prev
        


# @lc code=end

