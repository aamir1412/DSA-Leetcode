class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def dfs(x, y, prevht, seen):
            if (x < 0 or x >= ROWS or y < 0 or y >= COLS or 
                (x, y) in seen or prevht > heights[x][y]):
                return
            prevht = heights[x][y]
            seen.add((x, y))
            for r, c in moves:
                r, c = (r + x), (c + y)
                dfs(r, c, prevht, seen)
                
        for r in range(ROWS):
            dfs(r, 0, 0, pac)
            dfs(r, COLS-1, 0, atl)             
            
        for c in range(COLS):
            dfs(0, c, 0, pac)
            dfs(ROWS-1, c, 0, atl)
                
        res = []
        for cell in pac:
            if cell in atl:
                res.append(cell)
        return res
            
        
                
                