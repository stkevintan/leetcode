#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import Counter, List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return self.count(nums)
        return self.boyerMoore(nums)
    
    # hashtable
    def count(self, nums: List[int]) -> int:
        d = Counter(nums)
        return [x for x in d if d[x] * 2 > len(nums)][0]
    
    # select the first one as a candidate and set its vote to 1 then iterate forward, 
    # if current item equals to the candidate, its vote plus 1, otherwise vote subtract 1
    # if the vote become zero, which means the candidate's count is equals than other numbers. no number can be mode
    # then we select the next number as the candidate and set its vote 1, repeat the process until the list end.
    def boyerMoore(self, nums: List[int]) -> int:
        candidate = -1
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        # This question promise there always exist a mode
        # if count > 0:
        return candidate

# @lc code=end

