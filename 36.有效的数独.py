#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
from typing import List, Tuple


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            acc = 0
            for cell in row:
                if cell == '.':
                    continue
                bit = 1 << int(cell)
                if acc & bit > 0:
                    return False
                acc = acc ^ bit
        
        for col in range(0, 9):
            acc = 0
            for row in range(0, 9):
                if board[row][col] == '.':
                    continue
                bit = 1 << int(board[row][col])
                if acc & bit > 0:
                    return False
                acc = acc ^ bit
        
        for grid in range(0, 9):
            acc = 0
            r, c = self.getBlockStartCell(grid)
            for row in range(r, r + 3):
                for col in range(c, c + 3):
                    if board[row][col] == '.':
                        continue
                    bit = 1 << int(board[row][col])
                    if acc & bit > 0:
                        return False
                    acc = acc ^ bit
        return True

    def getBlockStartCell(self, grid: int) -> Tuple[int, int]:
        x = (grid % 3) * 3
        y = (grid // 3) * 3
        return x, y


# @lc code=end

