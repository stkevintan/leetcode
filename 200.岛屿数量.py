#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

from typing import List, Tuple
# @lc code=start


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        self.n, self.m = n, m
        self.parent = [[(-1, -1) for _ in range(m)] for _ in range(n)]
        # describe how deep of current tree
        self.rank = [[0] * m for _ in range(n)]
        self.count = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '1':
                    self.parent[i][j] = (i, j)
                    self.count += 1

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '1':
                    grid[i][j] = '0'
                    for dx, dy in dirs:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < m and grid[x][y] == '1':
                            self.union((x, y), (i, j))

        return self.count

    def union(self, fr: Tuple[int, int], to: Tuple[int, int]) -> None:
        frRoot = self.find(fr)
        toRoot = self.find(to)
        if frRoot != toRoot:
            xf, yf = frRoot
            xt, yt = toRoot
            if self.rank[xf][yf] > self.rank[xt][yt]:
                self.parent[xt][yt] = frRoot
            elif self.rank[xf][yf] < self.rank[xt][yt]:
                self.parent[xf][yf] = toRoot
            else:  # same depth
                self.parent[xf][yf] = toRoot
                # the root becoming deeper
                self.rank[xt][yt] += 1
            self.count -= 1

    def find(self, coord: Tuple[int, int]) -> Tuple[int, int]:
        x, y = coord
        return self.parent[x][y] if self.parent[x][y] == (x, y) else self.find(self.parent[x][y])


# @lc code=end
