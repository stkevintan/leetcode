#
# @lc app=leetcode.cn id=419 lang=python3
#
# [419] 甲板上的战舰
#

from typing import List
# @lc code=start


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                if cell == 'X':
                    ans += 1
        return ans
# @lc code=end

