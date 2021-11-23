#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
from typing import List


class Node:
    
    def __init__(self, l: int, r: int) -> None:
        # denote from the LISs among nodes in this range.
        # Note: all the maxLen(LIS) are start from 0 not self.l
        self.maxLen = 0
        self.l = l
        self.r = r
        self.lson = None 
        self.rson = None 

    def mid(self) -> int: 
        return (self.l + self.r) >> 1


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return self.DP2(nums)
        return self.SegTree(nums)

     # 二分+dp
    # f[i] **当前**长度为i的LIS中最小的末尾元素，随着遍历nums不断维护
    def DP2(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n;
        maxLen = 0
        for i in range(0,n):
            if maxLen == 0 or nums[i] > f[maxLen - 1]:
                f[maxLen] = nums[i]
                maxLen += 1
            else:
                j = self.lowerBound(f[:maxLen], nums[i])
                f[j] = nums[i]
        return maxLen
        
    
    def lowerBound(self, arr: List[int], target: int) -> int:
        L, R = 0, len(arr)
        while L < R:
            M = (L + R) >> 1
            if arr[M] < target:
                L = M + 1
            else:
                R = M
        return L
# -----------------------------------------------------------    
    def SegTree(self, nums: List[int])-> int:
        # 可以离散化，节省空间
        (start, end) = (min(nums), max(nums))
        # we build more node ahead of start because we will query `num - 1` below`
        rt = self.build(start - 1, end)
        ans = 0
        for num in nums:
            current = self.query(rt, start, num - 1) + 1
            ans = max(ans, current)
            self.update(rt, num, current)
        return ans
    
    def build(self, l: int, r: int) -> Node:
        node = Node(l ,r)
        if l == r:
            return node
        m = node.mid()
        node.lson = self.build(l, m)
        node.rson = self.build(m + 1, r)
        # push_up(node)
        return node
    
    def query(self, rt: Node, L: int, R: int) -> int:
        if L <= rt.l and rt.r <= R:
            return rt.maxLen
        m = rt.mid()
        ans = 0
        if L <= m:
            # 这里不能 self.query(rt.rson ,L ,m) 因为R有可能小于m
            ans = max(ans, self.query(rt.lson, L, R))
        if m < R:
            ans = max(ans, self.query(rt.rson, L, R))
        return ans 
    
    def update(self, rt: Node, pos: int, val: int):
        if rt.l == rt.r == pos:
            rt.maxLen = val
            return
        m = rt.mid()
        if pos <= m:
            self.update(rt.lson, pos, val)
        else:
            self.update(rt.rson, pos, val)
        self.push_up(rt)

    def push_up(self, rt: Node):
        rt.maxLen = max(rt.lson.maxLen, rt.rson.maxLen)
# @lc code=end

