class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:        
        visit = set()
        adj = {i:[] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        print(adj)            
        def dfs(v):            
            if v in visit:
                return
            
            visit.add(v)            
            for i in adj[v]:
                dfs(i)
        
        count = 0
        for i in range(n):            
            if i not in visit:                  
                dfs(i)                
                count += 1                
        return count
            