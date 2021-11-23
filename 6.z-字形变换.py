#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
# Note 1: numRows: 1 is different with others. 
# numRows > 1: number counts of down and up are the same.  
# numRows == 1: number counts of up is 1 but down is 0.

# version 1:
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
        # chars = []
        # for i in range(0, min(len(s), numRows)):
        #   # i -> down    + up     |  up      + down
        #   # 0 -> (n - 1) + (n - 1) | (n - n) + (n - n))
        #   # 1 -> (n - 2) + (n - 2) | (n - (n - 1)) + (n - (n - 1))
        #   # 2 -> (n - 3) + (n - 3) | (n - (n - 2)) + (n - (n - 2))
        #   # ...
        #   # k -> 2 * (n - (k + 1)) | 2 * (n - (n - k))
        #   # ...
        #   # n - 1 -> 2 * (n - n)   | 2 * (n - 1)
        #     k = i
        #     dis = [
        #         # 2 * (n - (k + 1))
        #         2 * (numRows - k - 1),
        #         # 2 * (n - (n - k))
        #         2 * k
        #     ]
            
 
        #     p = 0
        #     while k < len(s):
        #         chars.append(s[k])
        #         # when dis[p] and dis[1 - p] both are 0, it must be the case of numRows == 1
        #         k += dis[p] if dis[p] > 0 else dis[1 - p] if dis[1 - p] > 0 else 1
        #         p = 1 - p

        # return ''.join(chars)

# version 2:
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        chars = []
        for r in range(0, min(len(s), numRows)):
                top = 0
                while top - r < len(s):
                    prev, next = top - r, top + r
                    if prev >= 0:
                        chars.append(s[prev])
                    if r != 0 and r != numRows - 1 and next < len(s):
                        chars.append(s[next])
                    top += 2 * (numRows - 1)
        return ''.join(chars)


# @lc code=end
