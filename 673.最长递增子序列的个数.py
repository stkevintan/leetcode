#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

from typing import List, Tuple
# @lc code=start


class Node:
    def __init__(self, l: int, r: int) -> None:
        self.l = l;
        self.r = r;
        self.len = 0;
        self.cnt = 0;
        self.lson = None;
        self.rson = None;

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # return self.DP2(nums)
        return self.SegTree(nums)

    # 朴素dp:
    # f[i] = max(f[j]) + 1 (nums[j] < nums[i])  以第i个元素结尾的LIS
    # g[i] 以第i元素结尾最长LIS的数量
    def DP1(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1] * (n + 1)
        g = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                if nums[j - 1] < nums[i - 1]:
                    if f[i] == f[j] + 1:
                        g[i] += g[j]
                    elif f[i] < f[j] + 1:
                        f[i] = f[j] + 1
                        g[i] = g[j]
        maxlen = max(f[1:])
        ans = 0
        for i in range(1, n+1):
            if f[i] == maxlen:
                ans += g[i]
        return ans
#==================================================================================================
    # 二分+双dp
    # f[i]代表长度为i的LIS所有的可能结尾（一个倒序排列的数组，最后一个即为最小）
    # cnt[i][j] 代表长度为i的LIS,结尾为f[i][j]的种类
    # prefixCnt[i]: 为了快速计算cnt[i]中某一段的和，我们将cnt[i]数组保存为前缀和的形式
    def DP2(self, nums: List[int]) -> int:
        n = len(nums)
        f = []
        prefixCnt = []
        for i in range(0, n):
            if i == 0:
                f.append([nums[0]])
                prefixCnt.append([1])
                continue
            if nums[i] > f[-1][-1]: # append
                index = self.rbinarySearch(f[-1], nums[i])
                prefixCnt.append([prefixCnt[-1][-1] - (0 if index == 0 else prefixCnt[-1][index - 1])])
                f.append([nums[i]])
            else:
                index = self.lbinarySearch(f, nums[i])
                f[index].append(nums[i])
                curcnt = 1
                if index != 0:
                    index2 = self.rbinarySearch(f[index - 1], nums[i])
                    curcnt = prefixCnt[index - 1][-1] - (0 if index2 == 0 else prefixCnt[index - 1][index2 - 1])
                prefixCnt[index].append(prefixCnt[index][-1] + curcnt)
        return prefixCnt[-1][-1]

    def rbinarySearch(self, arr: List[int], target: int) -> int:
        L, R = 0, len(arr)
        while L < R:
            M = (L + R) >> 1
            if arr[M] >= target:
                L = M + 1
            else:
                R = M
        return L

    def lbinarySearch(self, arr: List[List[int]], target: int) -> int:
        L, R = 0, len(arr)
        while L < R:
            M = (L + R) >> 1
            if arr[M][-1] < target:
                L = M + 1
            else:
                R = M
        return L

#======================================================================================
    def SegTree(self, nums: List[int]) -> int:
        mp = nums[:]
        mp.sort()
        #unique the mp
        n = 0
        for i in range(0, len(mp)):
            if i == 0 or mp[i] != mp[i - 1]:
                mp[n] = mp[i]
                n+=1
        rt = self.build(0, n)
        maxLen = maxCnt = 0
        for num in nums:
            x = self.bin(num, mp, n)
            length, cnt = self.query(rt, 0, x - 1) if x > 0 else (0 , 1)
            # Note: cnt should at least 1
            cnt = max(cnt, 1)
            if maxLen < length + 1:
                maxLen = length + 1
                maxCnt = cnt
            elif maxLen == length + 1:
                maxCnt += cnt
            self.update(rt, x, length + 1, cnt)
        return maxCnt
    
    def bin(self, value: int, arr: List[int], n: int) -> int:
        L, R = 0, n
        while L < R:
            M = (L + R) >> 1
            if arr[M] < value:
                L = M + 1
            else:
                R = M
        return L

    def build(self, l: int, r: int) -> Node:
        node = Node(l ,r)
        if l == r:
            return node
        m = (node.l + node.r) >> 1
        node.lson = self.build(l, m)
        node.rson = self.build(m + 1, r)
        self.pushUp(node)
        return node
    
    def query(self, rt: Node, L: int, R: int) -> Tuple[int, int]:
        if L <= rt.l and rt.r <= R:
            return (rt.len, rt.cnt)
        m = (rt.l + rt.r) >> 1
        len1 = len2 = cnt1 = cnt2 = 0
        if L <= m:
            len1, cnt1 = self.query(rt.lson, L ,R)
        if m < R:
            len2, cnt2 = self.query(rt.rson, L, R)
        if len1 < len2:
            return (len2, cnt2)
        if len1 > len2:
            return (len1, cnt1)
        return (len1, cnt1 + cnt2)

    def update(self, rt: Node, pos: int, length: int, cnt: int):
        if rt.l == rt.r:
            # Note: sum up the incoming cnt if length is the same.
            if rt.len == length:
                rt.cnt += cnt
            else:
                rt.len = length
                rt.cnt = cnt
            return
        m = (rt.l + rt.r) >> 1
        
        if pos <= m:
            self.update(rt.lson, pos, length, cnt)
        else:
            self.update(rt.rson, pos, length, cnt)
        self.pushUp(rt)
    
    def pushUp(self, rt: Node):
        if rt.lson.len == rt.rson.len:
            rt.len = rt.lson.len
            rt.cnt = rt.lson.cnt + rt.rson.cnt
        elif rt.lson.len < rt.rson.len:
            rt.len = rt.rson.len
            rt.cnt = rt.rson.cnt
        else:
            rt.len = rt.lson.len
            rt.cnt = rt.lson.cnt



# @lc code=end
