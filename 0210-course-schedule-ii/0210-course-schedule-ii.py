class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen, cycle = set(), set()
        res = []
        preq = {c:[] for c in range(numCourses)}
        for x, y in prerequisites:
            preq[x].append(y)
            
        # print(preq)
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return
            
            cycle.add(crs)
            for c in preq[crs]:
                if dfs(c) == False:
                    return False
                
            cycle.remove(crs)                
            res.append(crs)
            seen.add(crs)
            
        for x in range(numCourses):
            if dfs(x) == False:
                return []
            
        return res
            
        