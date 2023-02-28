class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {c:[] for c in range(numCourses)}
        for x, y in prerequisites:
            preq[x].append(y)
            
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            
            if preq[crs] == []:
                return True
            
            cycle.add(crs)
            for c in preq[crs]:
                if dfs(c) == False:
                    return False
            
            cycle.remove(crs)
            preq[crs] = []
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return False
        return True