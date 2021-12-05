#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#

# @lc code=start
from typing import List
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        return self.djkstra1(times, n, k)

    #  we split the whole node into two kinds: determined and undetermined,
    #  at first, all nodes are undermined
    #  everytime, we select an undermined node with a minimal dist,
    #  mark it determined, use it to refersh the dist of its adjacent nodes
    #  repeat the above step until all nodes are determined
    def djkstra1(self, times: List[List[int]], n: int, k: int) -> int:
        G = [[float('inf')] * n for _ in range(n)]
        dist = [float('inf')] * n
        used = [False] * n
        for [u, v, w] in times:
            G[u - 1][v - 1] = w
        dist[k - 1] = 0
        for _ in range(n):
            # find the min index
            du, u = min([(d, i) for i, d in enumerate(dist) if not used[i]])
            for v in range(n):
                if u != v and dist[v] > du + G[u][v]:
                    dist[v] = du + G[u][v]
            used[u] = True
        ans = max(dist)

        return ans if ans < float('inf') else -1

    # if it is a sparse graph (nodes >> edges), we can store the edges
    # we also can use a priority queue to fast select the minimal node
    def djkstra2(self, times: List[List[int]], n: int, k: int) -> int:
        E = [[] for _ in range(n)]
        used = [False] * n
        dist = [float('inf')] * n
        for [u, v, w] in times:
            E[u - 1].append((v - 1, w))
        dist[k - 1] = 0
        pq = [k - 1]
        used[k - 1] = True
        while pq:
            u = heappop(pq)
            for v, w in E[u]:
                if not used[v] and dist[v] > (d := dist[u] + w):
                    used[v], dist[v] = True, d
                    heappush(pq, v)
        ans = max(dist)
        return ans if ans < float('inf') else -1


# @lc code=end
