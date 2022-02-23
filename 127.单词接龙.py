#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
from typing import Iterable, List, Tuple
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        beginIndex, endIndex = -1, -1
        for i, word in enumerate(wordList):
            if word == beginWord:
                beginIndex = i
            if word == endWord:
                endIndex = i
        if endIndex == -1:
            return 0
        # append beginWord to list in order to discrete
        if beginIndex == -1:
            wordList.append(beginWord)
            beginIndex = len(wordList) - 1

        steps = [0] * len(wordList)
        forwardQ, backwardQ = deque([beginIndex]), deque([endIndex])        
        # positive value means Q1, negative value means Q2
        steps[beginIndex], steps[endIndex] = 1, -1

        Q = forwardQ
        while forwardQ and backwardQ:
            index = Q.popleft()
            step = steps[index]
            validWordList = [(i, word) for i, word in enumerate(wordList) if steps[i] * step <= 0]
            for i in self.adjacents(validWordList, wordList[index]):
                if steps[i] * step < 0:
                    return abs(steps[i]) + abs(step)
                steps[i] = step + 1 if step > 0 else step - 1
                Q.append(i)
            # switch current Queue
            Q = backwardQ if Q == forwardQ else forwardQ
        return 0

    def adjacents(self, wordList: List[Tuple[int, str]], target: str) -> Iterable[int]:
        for i, word in wordList:
            diff = sum([1 if target[i] != word[i] else 0 for i in range(len(target))])
            if diff == 1:
                yield i

# @lc code=end
