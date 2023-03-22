from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        def dfs(curr, adj, visited, res):
            visited[curr] = True
            if curr in adj:
                for n, cost in adj[curr]:
                    res = min(res, cost)
                    if not visited[n]:
                        res = min(dfs(n, adj, visited, res), res)
            return res
        adj = defaultdict(list)
        for a, b, cost in roads:
            adj[a].append([b, cost])
            adj[b].append([a, cost])
        visited = [False] * (n + 1)
        res = dfs(1, adj, visited, float("inf"))
        return res