#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import Iterator, List, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i -1]:
                continue
            
            for arr in self.twoSum(nums[i+1:], -nums[i]):
                ret.append([nums[i], *arr])
        return ret

    def twoSum(self, nums: List[int], target: int) -> Iterator[Tuple[int, int]]:
        l, r = 0, len(nums) - 1
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                yield nums[l], nums[r]
                while l < r and nums[l + 1] == nums[l]:
                    l += 1
                while l < r and nums[r - 1] == nums[r]:
                    r -= 1
                l += 1
                r -= 1
            elif sum < target:
                l += 1
            else:
                r -= 1


# @lc code=end

