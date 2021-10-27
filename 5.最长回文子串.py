#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        f = [[False] * n for _ in range(n)]
        ans = ''
        ansLen = 0
        for k in range(n):
            for i in range(n):
                j = i + k
                if j >= n:
                    break
                if s[i] == s[j]:
                    f[i][j] = True if i + 1 > j - 1 else f[i + 1][j - 1]
                else:
                    f[i][j] = False
                if f[i][j] and ansLen < j - i + 1:
                    ansLen = j - i + 1
                    ans = s[i:j + 1]
        return ans


# @lc code=end

