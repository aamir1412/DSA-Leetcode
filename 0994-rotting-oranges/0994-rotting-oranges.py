class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = set()
        fresh, time = 0, 0
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        dq = collections.deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    dq.append((i, j))
                    seen.add((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        while dq and fresh > 0:            
            for i in range(len(dq)):                
                x, y = dq.popleft()            
                for r, c in moves:
                    r, c = (r + x), (c + y)
                    if (r >= 0 and r < ROWS and c >= 0 and c < COLS and
                       (r, c) not in seen and grid[r][c] == 1):
                        dq.append((r, c))
                        seen.add((r, c))
                        fresh -= 1
            time += 1  
        return time if fresh == 0 else -1
        
        
        