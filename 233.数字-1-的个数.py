#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#

# @lc code=start
from math import prod


class Solution:
    def countDigitOne(self, n: int) -> int:
        # return self.digitDp(n)
        return self.math(n)
    
    def digitDp(self, n: int) -> int:
        self.s = str(n)
        self.lenS = len(self.s)
        self.dp = [0] * (self.lenS)
        for i in range(1, self.lenS):
            # 0 ~ 9 + rest
            self.dp[i] += 10 * self.dp[i - 1]
            # 1xx
            self.dp[i] += 10 ** (i - 1)
        
        return self.countX(0)

    
    def countX(self, i: int) -> int:
        if i >= self.lenS:
            return 0
        ans = 0
        c = self.s[i]
        rest = self.lenS - i - 1
        x = (ord(c) - ord('0'))
        if x > 1:
            # 0 ~ x - 1
            ans += self.dp[rest] * x
            # 1xxx
            ans += 10 ** rest
            # x
            ans += self.countX(i + 1)
        elif x == 1:
            # 0 
            ans += self.dp[rest]
            # 1
            ans += self.countX(i + 1) 
            # 1xxxx
            ans += 1 + (int(self.s[i + 1:]) if i < self.lenS - 1 else 0)
        else:
            ans += self.countX(i + 1)
        return ans
        

    # consider count of 1 for every digit separately
    def math(self, n: int) -> int:
        ans, base = 0, 1
        while n >= base:
            high, low = divmod(n, base * 10)
            ans += high * base
            if low >= 2 * base:
                ans += base
            elif low >= base:
                ans += low - base + 1
            base *= 10
        return ans

# @lc code=end

