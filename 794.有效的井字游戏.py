#
# @lc app=leetcode.cn id=794 lang=python3
#
# [794] 有效的井字游戏
#

# @lc code=start
from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xcount, ocount = 0, 0
        for row in board:
            for c in row:
                if c == 'X':
                    xcount += 1
                if c == 'O':
                    ocount += 1

        if xcount != ocount and xcount != ocount + 1:
            return False
        
        def hasWin(c: str):
            for i in range(3):
                if board[i] == c * 3:
                    return True
            for j in range(3):
                if board[0][j] + board[1][j] + board[2][j] == c * 3:
                    return True
            if board[0][0] + board[1][1] + board[2][2] == c * 3:
                return True
            if board[0][2] + board[1][1] + board[2][0] == c * 3:
                return True
            return False
        
        xWin, oWin = hasWin('X'), hasWin('O')

        if xWin and oWin:
            return False
        
        if xWin:
            return xcount == ocount + 1
        if oWin:
            return xcount == ocount
        
        return True


# @lc code=end

