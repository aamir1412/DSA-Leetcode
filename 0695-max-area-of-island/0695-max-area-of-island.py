class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        maxx = [0]
        
        def bfs(x, y):
            dq = collections.deque()
            dq.append((x, y))
            count = 1
            while(dq):
                (x, y) = dq.popleft()
                for r, c in moves:
                    r, c = (r + x), (c + y)
                    if (r >= 0 and r < ROWS and c >= 0 and c < COLS and 
                        grid[r][c] == 1 and (r, c) not in seen):
                        dq.append((r, c))
                        seen.add((r, c))
                        count += 1 
            maxx[0] = max(count, maxx[0])            
                        
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in seen and grid[i][j] == 1:
                    seen.add((i, j))
                    bfs(i, j)
        
        return maxx[0]     
                        
                