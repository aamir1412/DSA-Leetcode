class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()        
        time, fresh = 0, 0
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1  
                if grid[i][j] == 2:
                    q.append((i, j))
        
        while q and fresh > 0:
            for i in range(len(q)):                    
                x, y = q.popleft()                    
                for r, c in moves:
                    r += x
                    c += y
                    if ((r >= 0 and r < ROWS) and (c >= 0 and c < COLS) and 
                        ((r, c) not in visit and grid[r][c] == 1)):
                        q.append((r, c))
                        visit.add((r, c))
                        fresh -= 1
            time += 1    
            
        return time if fresh == 0 else -1
        
         