class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        move = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def dfs(x, y, prvht, visit):
            if ((x < 0 or x >= ROWS) or
                (y < 0 or y >= COLS) or 
                ((x, y) in visit or heights[x][y] < prvht)):
                return
            prvht = heights[x][y]
            visit.add((x,y))
            for (r, c) in move:
                r += x
                c += y
                dfs(r, c, prvht, visit)
                
        for c in range(COLS):
            dfs(0, c, 0, pac)
            dfs(ROWS-1, c, 0, atl)
        
        for r in range(ROWS):
            dfs(r, 0, 0, pac)
            dfs(r, COLS-1, 0, atl)
        
        res = []
        for x in pac:
            if x in atl:
                res.append(x)
        
        res.sort()        
        return res
        
                