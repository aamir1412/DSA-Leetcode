class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i:[] for i in range(numCourses)}
        for x, y in prerequisites:
            preq[x].append(y)        
        seen = set()
        
        def dfs(crs):
            if crs in seen:
                return False
            
            if preq[crs] == []:
                return True
            
            seen.add(crs)
            for c in preq[crs]:
                if dfs(c) == False:
                    return False
            seen.remove(crs)
            preq[crs] = []
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True