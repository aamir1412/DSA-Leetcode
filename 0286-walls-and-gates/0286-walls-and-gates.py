class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        d = 0
        dq = collections.deque()
        seen = set()
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ROWS, COLS = len(rooms), len(rooms[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    dq.append((i, j))
                    seen.add((i, j))
        
        while dq:
            d += 1
            for i in range(len(dq)):
                x, y = dq.popleft()
                for r, c in moves:
                    r, c = (r + x), (c + y)
                    if (r >= 0 and r < ROWS and c >= 0 and c < COLS and 
                        (r, c) not in seen and rooms[r][c] > 0):
                        dq.append((r, c))
                        seen.add((r, c))
                        rooms[r][c] = d
        
        
                