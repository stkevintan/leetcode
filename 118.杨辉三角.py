#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

from typing import List
# @lc code=start


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            if i == 0:
                ans.append([1])
            else:
                tmp = [1]
                for i in range(1, len(ans[-1])):
                    tmp.append(ans[-1][i] + ans[-1][i - 1])
                tmp.append(1)
                ans.append(tmp)
        return ans

# @lc code=end

