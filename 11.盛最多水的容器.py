#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R, ans = 0, len(height) - 1, 0
        while L < R:
            HL, HR = height[L], height[R]
            ans = max(ans, (R - L) * min(HL, HR))
            if HL > HR:
                R -= 1
            else:
                L += 1
        return ans

    def maxArea2(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            if height[left] > height[right]:
                cur = height[right] * (right - left)
                if ans < cur:
                    ans = cur
                right-= 1
            else:
                cur = height[left] * (right - left)
                if ans < cur:
                    ans = cur
                left += 1
        return ans


# @lc code=end

