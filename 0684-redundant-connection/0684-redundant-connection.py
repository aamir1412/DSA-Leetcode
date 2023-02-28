class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def findPar(p):
            p = par[p]
            while p != par[p]:
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = findPar(n1), findPar(n2)
            
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]                
            return True
        
        for x, y in edges:
            if union(x, y) == False:
                return [x, y]
            
        