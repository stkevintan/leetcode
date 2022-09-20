#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
from typing import List

# @lc code=start


class Solution:
    def bound(self, at, size, target: int, lower: bool = True) -> int:
        L, R = 0, size
        while L < R:
            M = (L + R) >> 1
            if at(M) < target or (not lower and at(M) == target):
                L = M + 1
            else:
                R = M
        return L

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        colStart = self.bound(lambda i: matrix[n - 1][i], m, target)
        colEnd = self.bound(lambda i: matrix[0][i], m, target, False)
        if colStart > colEnd - 1:
            return False
        rowStart = self.bound(lambda i: matrix[i][colEnd - 1], n, target)
        rowEnd = self.bound(lambda i: matrix[i][0], n, target, False)
        if rowStart > rowEnd - 1:
            return False

        i, j = rowEnd - 1, colStart
        while i >= rowStart and j < colEnd:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
# @lc code=end
