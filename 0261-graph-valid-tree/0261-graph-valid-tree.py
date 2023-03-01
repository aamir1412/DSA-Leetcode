class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
            
        def find(p):
            p = par[p]
            while p != par[p]:
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
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
            if not union(x, y):
                return False
            n -= 1
            
        return n == 1