#
# @lc app=leetcode.cn id=423 lang=python3
#
# [423] 从英文中重建数字
#

# @lc code=start
from collections import Counter


class Solution:
    # https://leetcode-cn.com/problems/reconstruct-original-digits-from-english/solution/jian-dan-de-xian-xing-dai-shu-kuai-lai-f-6e01/
    # 求解,非齐次线性方程
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)
        return "0" * cnt["z"] + \
               "1" * (cnt["o"] - cnt["z"] - cnt["u"] - cnt["w"]) + \
               "2" * cnt["w"] + \
               "3" * (cnt["r"] - cnt["z"] - cnt["u"]) + \
               "4" * cnt["u"] + \
               "5" * (cnt["v"] - cnt["s"] + cnt["x"]) + \
               "6" * cnt["x"] + \
               "7" * (cnt["s"] - cnt["x"]) + \
               "8" * (cnt["t"] - cnt["w"] - cnt["r"] + cnt["z"] + cnt["u"]) + \
               "9" * ((cnt["n"] - cnt["s"] + cnt["x"] - cnt["o"] + cnt["z"] + cnt["u"] + cnt["w"]) // 2)

# @lc code=end

