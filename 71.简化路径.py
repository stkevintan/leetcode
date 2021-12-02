#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for frag in path[1:].split('/'):
            if frag == '' or frag == '.':
                continue
            # Please do not code like: if frag == '..' and len(stack) > 0
            if frag == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(frag)
        return '/' + '/'.join(stack)

# @lc code=end

