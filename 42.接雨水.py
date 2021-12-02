#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # return self.monotonicStack(height)
        # return self.dp(height)
        return self.greedy(height)
    
    # 维护一个单调递减的栈, 快速查找左右边界
    def monotonicStack(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(height)):
            while len(stack) > 0:
                if height[stack[-1]] < height[i]:
                    top = stack.pop()
                    if len(stack) > 0:
                        left = stack[-1]
                        right = i
                        ans += (min(height[left], height[right]) - height[top]) * (right - left - 1)
                elif height[stack[-1]] == height[i]:
                    stack.pop()
                else:
                    break
            stack.append(i)
        return ans

    # dp预处理
    def dp(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0] * n, [0] * n
        for i in range(n):
            if i > 0 and height[i] <= left[i - 1]:
                left[i] = left[i - 1]
            else:
                left[i] = height[i]
        for i in range(n - 1, -1, -1):
            if i < n - 1 and height[i] <= right[i + 1]:
                right[i] = right[i + 1]
            else:
                right[i] = height[i] 
        ans = 0
        for i in range(n):
            ans += min(right[i], left[i]) - height[i] 
        return ans

    def greedy(self, height: List[int]) -> int:
        n = len(height)
        L, R = 0, n - 1
        lMax, rMax = 0, 0
        ans = 0
        while L < R:
            if L == 0 or height[L] > lMax:
                lMax = height[L]
            if R == n - 1 or height[R] > rMax:
                rMax = height[R]
            # 确保lMax < height[R]
            if height[L] < height[R]:
                ans += lMax - height[L]
                L += 1
            # 确保rMax < height[L]
            else:
                ans += rMax - height[R]
                R -= 1
        return ans
 
                    

# @lc code=end

