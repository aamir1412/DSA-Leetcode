class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        graph = {i:[] for i in range(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(x, prev):
            if x in visit:
                return False
            
            visit.add(x)
            for i in graph[x]:
                if i == prev:
                    continue
                if dfs(i, x) == False:
                    return False
            return True
                
        return dfs(0, -99) and n == len(visit)
            
            