class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = [0]
        adj = {i:[] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)        
        
        seen = set()
        def dfs(v):
            if v in seen:
                return            
            seen.add(v)
            for x in adj[v]:                
                dfs(x)
            
        for i in range(n):
            if i in seen:
                continue
            dfs(i)
            count[0] += 1
                
        return count[0]
            
        