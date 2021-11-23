#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L, R = 0, n - 1
        self.nums, self.target = nums, target
        self.defaultCheckRet = 1 if self.isOnRight(target) else -1
        while L <= R:
            M = (L + R) >> 1
            ret = self.check(M)
            if ret == 0:
                return M
            if ret < 0:
                R = M - 1
            else:
                L = M + 1 
        return -1

    def check(self, M):
        if self.nums[M] == self.target:
            return 0
        if self.nums[M] > self.target and self.isIndexOnRight(M):
            return -1 # go left
        if self.nums[M] < self.target and not self.isIndexOnRight(M):
            return 1  # go right
        return self.defaultCheckRet
    
    def isOnRight(self, x):
        return x < self.nums[0]

    def isIndexOnRight(self, index):
        return self.isOnRight(self.nums[index])



# @lc code=end
