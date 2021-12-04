#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
from collections import deque
from typing import List


class Node:
    v: int
    next: int

class Solution:
    def addEdge(self, u: int, v: int) -> None:
        self.edges[self.index].v = v
        self.edges[self.index].next = self.head[u]
        self.head[u] = self.index 
        self.index += 1
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.numCourses, self.prerequisites = numCourses, prerequisites
        self.edges: List[Node] = [Node() for _ in prerequisites]
        self.head: List[int] = [-1] * numCourses
        self.index = 0

        for [v, u] in prerequisites:
            self.addEdge(u, v)

        # return self.dfsVersion()
        return self.bfsVersion()
    
    def dfsVersion(self):
        ans = []
        # 0 - not yet, 1 - processing, 2 - completed
        state = [0] * self.numCourses
        def topsort(u: int) -> bool:
            state[u] = 1
            i = self.head[u]
            while i != -1:
                v = self.edges[i].v
                if state[v] == 0 and not topsort(v):
                    return False
                if state[v] == 1:
                    return False
                i = self.edges[i].next
            # mark this node has completed, avoid travel again
            state[u] = 2
            # postorder to collect the node reversely
            ans.append(u)
            return True

        for course in range(self.numCourses):
            if 0 == state[course] and not topsort(course):
                return []
    
        return ans[::-1]
    
    def bfsVersion(self):
        ans = []
        # collect the indegree of each node
        indeg = [0] * self.numCourses
        for [v, _] in self.prerequisites:
            indeg[v] += 1
        Q = deque([v for v in range(self.numCourses) if indeg[v] == 0]) 
        while Q:
            u = Q.popleft()
            ans.append(u)
            i = self.head[u]
            while i != -1:
                v = self.edges[i].v
                indeg[v] -= 1
                if indeg[v] == 0:
                    Q.append(v)
                i = self.edges[i].next
        # do not forget to check the size
        return ans if len(ans) == self.numCourses else []


# @lc code=end

