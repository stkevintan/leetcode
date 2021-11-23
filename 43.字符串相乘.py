#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
from typing import List


# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         self.num1, self.num2, self.n1, self.n2 = num1, num2, len(num1), len(num2)
#         self.total: List[int] = []
#         for i in reversed(range(self.n1)):
#             c = self.num1[i]
#             curRet = self.multiplyByX(int(c))
#             self.sumUp(curRet, self.n1 - i - 1)

#         return self.formatNum(self.total)

    
#     def multiplyByX(self, c: int):
#         ret, carry = [], 0
#         for i in reversed(range(self.n2)):
#             x = int(self.num2[i]) 
#             cur = x * c + carry
#             carry, digit = divmod(cur, 10)
#             ret.append(digit)
#         if carry > 0:
#             ret.append(carry)
#         # print(self.num2, ' * ', c,' = ', self.formatNum(ret))
#         return ret
    
#     def sumUp(self, addend: List[int], offset: int):
#         addendIndex, totalIndex, carry = 0, offset, 0
#         while addendIndex < len(addend):
#             x = addend[addendIndex] 
#             self.expandTo(totalIndex)
#             y = self.total[totalIndex]
#             cur = x + y + carry
#             carry, digit = divmod(cur, 10)
#             self.total[totalIndex] = digit
#             addendIndex += 1
#             totalIndex += 1
#         if carry > 0:
#             self.expandTo(totalIndex)
#             self.total[totalIndex] = carry
        
#     def expandTo(self, index: int):
#         amount = index + 1 - len(self.total)
#         if amount > 0:
#             self.total.extend([0] * amount)
    
#     def formatNum(self, num: List[int]) -> str:
#         ret = ''.join(map(str, reversed(num))).lstrip('0')
#         return ret if len(ret) > 0 else "0"
        
            
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        zero = ord("0")
        n1, n2 = len(num1), len(num2)
        # the maximun possible length of the product (including the possible carry)
        product = [0] * (n1 + n2)
        for index1, c1 in enumerate(num1):
            x1 = ord(c1) - zero
            for index2, c2 in enumerate(num2):
                x2 = ord(c2) - zero
                product[index1 + index2 + 1] += x1 * x2
        # normalize the product
        carry = 0
        for index in range(n1 + n2 - 1, -1, -1):
            carry, product[index] = divmod(product[index] + carry, 10)

        # assert carry must be zero
        res = ''.join(map(lambda x: chr(x + zero), product)).lstrip('0')
        return res if res else "0"

# 0 * 0
# 9133 * 0
# @lc code=end

