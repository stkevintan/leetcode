#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#

# @lc code=start
from heapq import heappop, heappush
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # return self.priorityQ(matrix, k)
        return self.binarySearch(matrix, k)
    
    def priorityQ(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        Q = [(matrix[0][0], 0, 0)]
        vis = [[False] * n for _ in range(n)]
        vis[0][0] = True
        top = -1
        while Q and k:
            (val, x, y) = heappop(Q)
            top = val
            k -= 1
            if x + 1 < n and not vis[x + 1][y]:
                heappush(Q, (matrix[x + 1][y], x + 1, y))
                vis[x + 1][y] = True
            if y + 1 < n and not vis[x][y + 1]:
                heappush(Q, (matrix[x][y + 1], x, y + 1))
                vis[x][y + 1] = True
        return top
    
    # binary search the result
    def binarySearch(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        L, R = matrix[0][0], matrix[n - 1][n - 1] + 1
        # from the left-bottom corner to count the items which less or equals than x
        def countLq(x: int) -> int:
            i, j, count = n - 1, 0, 0
            while i >= 0 and j < n:
                if matrix[i][j] <= x:
                    # add all column
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            return count
        while L < R:
            M = (L + R) >> 1
            cnt = countLq(M)
            if cnt < k:
                L = M + 1
            else:
                R = M
        return L



# @lc code=end

