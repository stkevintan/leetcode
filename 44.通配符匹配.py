#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # f[i][j]  can s[0:i] p[0:j] match
        # f[i][j] = f[i-1][j - 1] (if s[i] == j[i] or j[i] == '?')
        #         = f[i - 1][j] (multiple) or f[i][j - 1](zero) (j[i] == '*')
        # To avoid p startswith '*', if p is prefix with "***", then f[0][1]~f[0][3] should be true
        s = 'x' + s
        p = 'x' + p
        # rolling list
        f = [[False, False] for _ in range(len(p) + 1)]
        cur = 0
        f[cur][0] = True
        for i in range(1, len(s) + 1):
            cur ^= 1
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    f[j][cur] = f[j - 1][cur ^ 1]
                elif p[j - 1] == '*':
                    f[j][cur] = f[j][cur ^ 1] or f[j - 1][cur]
                # attention
                else:
                    f[j][cur] = False
        return f[len(p)][cur]

# @lc code=end
