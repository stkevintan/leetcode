#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

from typing import List
from math import factorial
# @lc code=start


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # return self.nextPermutation(n, k)
        return self.RCantor(n, k)

    # reverse Cantor expansion 
    # https://oi-wiki.org/math/combinatorics/cantor/
    # 我们知道长为5的排列[2,5,3,4,1]大于以 1为第一位的任何排列，以 1 为第一位的 5 的排列有 4! 种。
    def RCantor(self, n: int, k: int) -> str:
        ans: List[str] = []
        p = n
        taken = [False] * (n + 1)
        while p:
            # there are k - 1 sequences less than current sequence
            # we divide it by the factorial of following digit count(n - 1 digits followed after n-th digit)
            # to get how many sequences have a strict smaller digit on that position 
            count, mod = divmod(k - 1, factorial(p - 1))
            # or use tree-like array to reduce the time complexity
            c = 0
            for i in range(1, n + 1):
                if not taken[i]:
                    c += 1
                if c == count + 1:
                    ans.append(chr(i + ord('0')))
                    taken[i] = True
                    break
            # k -= count * factorial(p - 1)
            k = mod + 1 # k - 1 = mod
            p -= 1
        return ''.join(ans)

    def nextPermutation(self, n: int, k: int) -> str:
        ans = [i for i in range(1, n + 1)]
        for _ in range(k - 1):
            if not self.next(ans):
                break
        return ''.join(map(str, ans))

    def next(self, ans: List[int]) -> bool:
        partitionIndex = len(ans) - 2
        while partitionIndex >= 0 and ans[partitionIndex] >= ans[partitionIndex + 1]:
                partitionIndex -= 1
        if partitionIndex < 0:
            # don't forget reverse the whole sequence
            self.reverse(ans, 0) 
            return False
        partition = ans[partitionIndex]
        changeIndex = -1
        for i in range(len(ans) - 1, partitionIndex, -1):
            if ans[i] > partition:
                changeIndex = i
                break
        ans[partitionIndex], ans[changeIndex] = ans[changeIndex], ans[partitionIndex]
        self.reverse(ans, partitionIndex + 1)
        return True
    
    def reverse(self, ans: List[int], start: int) -> None:
        L, R = start, len(ans) - 1
        while L < R:
            ans[L], ans[R] = ans[R], ans[L]
            L += 1
            R -= 1

# @lc code=end

