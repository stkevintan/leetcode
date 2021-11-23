#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

from typing import List
# @lc code=start


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        return self.DP1();

    # 朴素dp:
    # f[i] = max(f[j]) + 1 (nums[j] < nums[i])  以第i个元素结尾的LIS
    # g[i] 以第i元素结尾最长LIS的数量
    def DP1(self, nums: List[int]) -> int:
        n = len(nums);
        f = [1] * (n + 1)
        g = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                if nums[j - 1] < nums[i - 1]:
                    if f[i] == f[j] + 1:
                        g[i] += g[j];
                    elif f[i] < f[j] + 1:
                        f[i] = f[j] + 1;
                        g[i] = g[j];
        maxlen = max(f[1:])
        ans = 0;
        for i in range(1, n+1):
            if f[i] == maxlen:  
                ans+=g[i]
        return ans
    
    # 二分+dp
    # f[i] **当前**长度为i的LIS中最小的末尾元素，随着遍历nums不断维护
    def DP2(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n;
        index = 0
        for i in range(0,n):
            if i == 0 or nums[i] >= f[index]:
                f[index] = nums[i]
                index += 1
            else:
                j = self.binarySearch(f[:index], nums[i])
                f[j] = nums[i]
        
    
    def binarySearch(self, arr: List[int], target: int) -> int:
        L, R = 0, len(arr)
        while L < R:
            M = (L + R) >> 1
            if arr[M] < target:
                L = M + 1
            else:
                R = M
        return L



    # def SegTree(self, nums: List[int]) -> int:

# @lc code=end

