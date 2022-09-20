#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#

# @lc code=start
class Solution:
    # manacher
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        new_s = s + '#' + rev
        prefix = [0] * len(new_s)
        for i in range(1, len(new_s)):
            j = prefix[i - 1]
            while j > 0 and new_s[i] != new_s[j]: j = prefix[j - 1]
            if new_s[i] == new_s[j]: j += 1
            prefix[i] = j
        return rev[0: len(s) - prefix[len(new_s) - 1]] + s
# @lc code=end

