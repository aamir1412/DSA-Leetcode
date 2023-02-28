class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen, cycle = set(), set()
        res = []
        preq = {i:[] for i in range(numCourses)}        
        for x, y in prerequisites:
            preq[x].append(y)
            
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
            return True
        
        for i in range(numCourses):            
            if dfs(i) == False:
                return []
        return res
        
        
        
        