#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
# from ast import List


from typing import List

# 要点：
# 1. 本题最好将L, M, R看成**个数**。 我们将在nums1里面取多少个数在0 ~ Len(nums1)之间二分, 此时index = M  - 1
# 2. 不需要两个数组都二分，只需要二分其中一个，然后另外一个通过长度可以计算出来
# 3. 二分的时候，M1边界是安全的，但是M2边界不安全
# 4. 如果M1增大，那么M2一定是减小的，不可能两者同时很大或者很小
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums1, self.nums2 = nums1, nums2
        self.Len1, self.Len2 = len(nums1), len(nums2)
        self.Len = self.Len1 + self.Len2
        L, R = 0, self.Len1 + 1
        while L < R:
            M1, M2 = self.partition(L, R)
            if self.check(M1, M2):
                L = M1 + 1
            else:
                R = M1
        return self.getMedian(*self.partition(L, R))
    
    # 判断M1能否增加，相对应的M2能否减小
    def check(self, M1, M2):
        # 如果M2已经大于实际上能取的个数，则M2肯定是需要减小的, 根据第4条要点，M1可以安全的增大
        # 这里用了 > 而不能用 == 主要因为第三条要点
        if M2 > self.Len2:
            return True
        # 如果M1已经在极大位置了, 那么M1无法再增大了
        if M1 == self.Len1:
            return False
        # 如果M2已经在极小的位置了，那么M2无法再减小了
        # 这里必须 <= 0 而不能 == 0， 因为第三点
        if M2 <= 0:
            return False
        return self.nums1[M1] < self.nums2[M2 - 1]

    def partition(self, L, R):
        M1 = (L + R) >> 1
        # unsafe
        M2 = (self.Len >> 1) - M1
        return M1, M2
    
    def getMedian(self, M1, M2):
        if self.Len & 1:
            return self.rightMin(M1, M2)
        return (self.leftMax(M1, M2) + self.rightMin(M1, M2)) / 2
    
    def rightMin(self, M1, M2):
        if M1 == self.Len1:
            return self.nums2[M2]
        if M2 == self.Len2:
            return self.nums1[M1]
        return min(self.nums1[M1], self.nums2[M2])
    
    def leftMax(self, M1, M2):
        if M1 == 0:
            return self.nums2[M2 - 1]
        if M2 == 0:
            return self.nums1[M1 - 1]
        return max(self.nums1[M1 - 1], self.nums2[M2 - 1])
    
            
# print(Solution().findMedianSortedArrays([1,2,3,4,6], [5]))
# print(Solution().findMedianSortedArrays([2,3,4,5,6,7], [1]))
# @lc code=end

