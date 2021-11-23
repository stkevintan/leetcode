#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return [] 
        border = {
            "rowStart" : 0,
            "rowEnd": len(matrix) - 1,
            "colStart": 0, 
            "colEnd": len(matrix[0]) - 1
        }
        ret = []
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        turns = ['colStart', 'rowStart', 'colEnd', 'rowEnd']
        dirIndex = 0
        Q = [(0, 0)]
        def checkPoint(x, y):
            return border["rowStart"] <= x <= border["rowEnd"] and border["colStart"] <= y <= border["colEnd"]

        while len(Q) > 0: 
            x, y = Q.pop()
            ret.append(matrix[x][y])
            dir = dirs[dirIndex]
            x2 = x + dir[0]
            y2 = y + dir[1]
            if checkPoint(x2, y2):
                Q.append((x2, y2))
            else:
                dirIndex = (dirIndex + 1) % 4
                dir = dirs[dirIndex]
                x2 = x + dir[0]
                y2 = y + dir[1]
                if checkPoint(x2, y2):
                    Q.append((x2, y2))
                    turn = turns[dirIndex]
                    border[turn] += dir[0] if dir[0] != 0 else dir[1]
        return ret
# @lc code=end

