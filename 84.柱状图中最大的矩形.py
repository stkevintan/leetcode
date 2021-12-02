#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.largestRectangleArea1(heights)

    # 基本原理: 对于每一位i，如果我们向左遍历到left, 向右遍历到right刚好满足 h[left] < h[i] > h[right]. 那么以h[i]为高的矩形最大长度应该就是 right - left - 1
    # 为了快速得到left，我们可以把已经遍历过的元素坐标记录到一个数组S里，但实际上我们并不需要完全记录: 比如说 2 5 3
    # i. 如果下一个元素是4 (h[i] > h[top])，那么完全往前找到3即可, 不用向前找5和2了。
    # ii. 如果下一个元素是1 (h[i] <= h[top])，那么找到3还需要继续向前查找的时候，我们已经知道当前元素一定不大于3了，因此实际上接下来我们只需要关心那些小于3的元素，5没必要记录，如果可以直接跳到2那么久节省了时间了。
    # 对于第二种情况，更common的说法就是对于S里面的数据反向查找时我们只需要从一个数跳到更小的数，从后向前减小那么就是从前向后单调递增。
    # 对于动态维护这个数组，我们应该使用栈的机制:
    # 当我们找到i的left, pop掉前面比i高的元素，将i压到S栈中（比如当前元素是3，S是[2, 4, 5], 那么4，5不再需要，应该pop掉，push当前的3进去，最终变成: [2, 3]）
    # 反过来我们可以得到每个元素的right, 最后遍历每个i，比较 h[i] * (right - left -1) 得到最大值即可
    def largestRectangleArea1(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n
        stack = []
        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if len(stack) > 0 else -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if len(stack) > 0 else n
            stack.append(i)

        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * (right[i] - left[i] - 1))
        return ans

    # 但实际上如果我们碰到一个元素i满足 h[i] > h[top] 直接push到栈里，不立刻处理它
    # 等到出现h[i] < h[top]触发pop时再去处理每个pop的元素，这个时候对于每个pop的元素i即是他们的right (h[i] < h[top]), left则是栈里排前面的那个元素(单调递增: h[top-1] < h[top])，因此可以一次性得出来pop元素的left，right
    # 这样处理的好处就是我们不需要开left和right数组了,坏处就是最后需要保证栈里的元素都会被pop干净（只在pop时候处理）
    def largestRectangleArea2(self, heights: List[int]) -> int:
        # 末尾添加一个绝对小的数保证最后所有的height都会被pop
        heights.append(-1)
        n = len(heights)
        stack = []
        ans = 0
        for i in range(n):
            while len(stack) > 0:
                if heights[stack[-1]] > heights[i]:
                    # 计算以第stack[k]个元素为中心左右各能够延申多长，保持高度不小于heights[stack[k]]
                    # 如果我们保证stack是严格递增的，那么最左能够延申到stack[k - 1]个元素, 因为严格比它高的元素已经pop了 (闭区间)
                    # 最右可以延申到i, 因为stack单调性，后面的元素都比它高直到第i个元素(闭区间)
                    # 最大范围: (stack[k - 1], i)
                    right = i
                    left = stack[-2] if len(stack) > 1 else -1
                    ans = max(ans, heights[stack[-1]] * (right - left - 1))
                    stack.pop()
                # 保持栈里面严格递增，此时不需要计算面积，因为肯定不是最大的(为了代码简洁也可以跟前面分支合在一起)
                elif heights[stack[-1]] == heights[i]:
                    stack.pop()
                else:
                    break
            if heights[i] != -1:
                stack.append(i)
        return ans

# @lc code=end
