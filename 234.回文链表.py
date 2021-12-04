#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

from typing import Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next
# @lc code=start
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        count = self.len(head) 
        if count == 1:
            return True 
        p1, p2 = self.reverse(head, count >> 1)
        head = p1
        if count & 1:
            p2 = p2.next
        def check():
            nonlocal p1, p2
            while p1 and p2:
                if p1.val != p2.val:
                    return False
                p1 = p1.next
                p2 = p2.next
            return True
        ret = check()
        # reverse the first half back
        self.reverse(head, count >> 1)
        return ret


    def len(self, head: ListNode)-> int:
        count = 0
        while head:
            head = head.next
            count += 1
        return count
    
    # reverse the first part
    def reverse(self, cur: ListNode, nodeCount: int) -> Tuple[ListNode, ListNode]:
        head = cur 
        times = nodeCount - 1
        while times > 0:
            next = cur.next
            next.next, cur.next = head, next.next
            head = next
            times -= 1
        return (head, cur.next)
    
    

        








# @lc code=end

