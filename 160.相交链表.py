#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        return self.getIntersectionNode2(headA, headB)
    
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA

    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        countA = self.getSize(headA)
        countB = self.getSize(headB)
        if countA < countB:
            headB = self.skip(headB, countB - countA)
        else:
            headA = self.skip(headA, countA - countB)
        while headA != headB and headA and headB:
            headA = headA.next
            headB = headB.next
        
        return headA
    
    def getSize(self, head: ListNode):
        count = 0
        while head:
            head = head.next
            count += 1
        return count
    
    def skip(self, head: ListNode, count: int) -> ListNode:
        while count and head:
            head = head.next
            count -= 1
        return head
        

        
# @lc code=end

