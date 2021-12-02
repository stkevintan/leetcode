#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

from typing import List
# @lc code=start


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        X: List[List[int]] = []
        for row in matrix:
            X.append([])
            for col in row:
                x = ord(col) - ord('0')
                X[-1].append(X[-1][-1] + 1 if len(X[-1]) > 0 and x == 1 else x)

        # add -1 to every column to pop up the stack below.
        X.append([-1] * m)
        ans = 0
        for j in range(m):
            stack = []
            getX = lambda index: X[index][j]
            for i in range(n + 1):
                x = getX(i)
                while len(stack) > 0:
                    if  getX(stack[-1]) > x:
                        topX = getX(stack.pop())
                        # every element in stack, it's farest length should be the index of it's prev-subling element + 1 
                        # because all the previous elements higher than it are pop out already.
                        ans = max(
                            ans, (i - (stack[-1] + 1 if len(stack) > 0 else 0)) * topX)
                    # Note: pop duplicated items in stack, make stack strictly go up.
                    elif getX(stack[-1]) == x:
                        stack.pop()
                    else:
                        break
                # push current element index into stack, except for -1
                if x != -1:
                    stack.append(i)
        return ans
