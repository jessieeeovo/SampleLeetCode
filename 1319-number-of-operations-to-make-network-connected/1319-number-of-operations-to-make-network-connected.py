class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        # create adjacency list
        adj = dict()
        for a, b in connections:
            if a not in adj:
                adj[a] = []
            adj[a].append(b)
            if b not in adj:
                adj[b] = []
            adj[b].append(a)
            
        def dfs(a):
            visited[a] = True
            if a not in adj:
                return
            for b in adj[a]:
                if not visited[b]:
                    visited[b] = True
                    dfs(b)
            
        numParts = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                numParts += 1
                dfs(i)
        return numParts - 1