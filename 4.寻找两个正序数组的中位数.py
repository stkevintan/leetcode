#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
# from ast import List


from typing import List


# 要点：
# 1. 不需要两个数组都二分，只需要二分其中一个，然后另外一个通过长度可以计算出来
# 2. 二分的时候，M1边界是安全的，但是M2边界不安全，需要适当调整
# 3. 先考虑往右往左的情况，那么剩下的情况一定是复合的情况
# 4. 往右往左的时候思考一下能否继续就行
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        Len1, Len2 = len(nums1), len(nums2)
        Len = Len1 + Len2
        # 本题最好将L, M, R看成**个数**。 我们将在nums1里面取多少个数在0 ~ Len(nums1)之间二分
        L1, R1 = 0, Len1
        
        def rightMin(M1, M2):
            if M2 >= Len2:
                return nums1[M1]
            elif M1 >= Len1:
                return nums2[M2]
            else:
                return min(nums2[M2], nums1[M1])
            
        def leftMax(M1, M2):
            if M1 - 1 < 0:
                return nums2[M2 - 1]
            elif M2 - 1 < 0:
                return nums1[M1 - 1]
            else:
                return max(nums1[M1 - 1], nums2[M2 - 1])

        def calc(M1, M2):
            if Len & 1:
                return rightMin(M1, M2)
            else:
                return (leftMax(M1, M2) + rightMin(M1, M2)) / 2

        while L1 <= R1:
            M1 = (L1 + R1) >> 1
            M2 = (Len >> 1) - M1
            # # M2 是不安全的，需要微调这个范围
            # if M2 < 0:
            #     M1, M2 = (Len >> 1), 0
            # if M2 > Len2:
            #     M1, M2 = (Len >> 1) - Len2, Len2
            # 或者过大了直接出发M1右移，过小了直接触发M1左移，更简洁但是效率更低
            # 准备往右缩小范围的时候先看一下是否能够往右 
            if M2 - 1 >= Len2 or M2 - 1 >= 0 and M1 < Len1 and nums2[M2 - 1] > nums1[M1]:
                L1 = M1 + 1
            # 准备往左缩小范围的时候先看一下能否往左 
            elif M2 < 0 or M1 - 1 >= 0 and M2 < Len2 and nums1[M1 - 1] > nums2[M2]:
                R1 = M1
            else:
                return calc(M1, M2)


# print(Solution().findMedianSortedArrays([1,2,3,4,6], [5]))
# print(Solution().findMedianSortedArrays([2,3,4,5,6,7], [1]))
# @lc code=end

