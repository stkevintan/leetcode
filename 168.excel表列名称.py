#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans: str = []
        while columnNumber > 0:
            columnNumber, mod = divmod(columnNumber, 26)
            # we don't allow 0, so we need handle following case:
            # (0 * 26^0 + B * 26^1 + C * 26^2 + ...) % 26  rewrite it to:
            # (26 * 26^0 + (B - 1) * 26^1 + C * 26^2 + ...) % 26 => (B * 26^0 + C * 26^1 + ...) - 1  ... 26
            if mod == 0:
                ans.append('Z')
                columnNumber -= 1
            else:
                ans.append(chr(mod + ord('A') - 1))

        return ''.join(reversed(ans))
# @lc code=end

