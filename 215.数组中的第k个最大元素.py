#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

from typing import List
from random import randint
from heapq import heapify, heappop, heappush, heapreplace
# @lc code=start


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.n = len(nums)
        return self.quickSelect(0, self.n - 1, self.n - k)

# ----------------------------
    def heap(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: -x, nums))
        heapify(nums)
        ans = 0
        while k:
            ans = -heappop(nums)
            k -= 1
        return ans
#----------------------------
    # priority queue, keep it always in k size
    def priorityQueue(self, nums: List[int], k: int) -> int: 
        pq = []
        for x in nums:
            if len(pq) < k:
                heappush(x)
            elif pq[0] < x:
                heapreplace(x)
        return pq[0]

#------------------------------
    def quickSelect(self, L: int, R: int, k: int) -> int:
        while L <= R:
            pivot = self.randomPartition(L, R)
            if pivot == k:
                return self.nums[pivot]
            elif pivot < k:
                L  = pivot + 1
            else:
                R = pivot - 1
    
    def partition(self, L: int, R: int) -> int:
        while L < R:
            P = L + 1
            if self.nums[L] < self.nums[P]:
                self.nums[P], self.nums[R] = self.nums[R], self.nums[P]
                R -= 1
            else:
                self.nums[L], self.nums[P] = self.nums[P], self.nums[L]
                L += 1
        return L

    def randomPartition(self, L: int, R: int) -> int:
        P = randint(L, R)
        boundary = L
        self.nums[P], self.nums[R] = self.nums[R], self.nums[P]
        for i in range(L, R):
            if self.nums[i] < self.nums[R]:
                self.nums[boundary], self.nums[i] = self.nums[i], self.nums[boundary]
                boundary += 1
        self.nums[boundary], self.nums[R] = self.nums[R], self.nums[boundary]
        return boundary

# @lc code=end

