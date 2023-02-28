class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visit = set()
        ROWS, COLS = len(board), len(board[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(x, y):               
            q = collections.deque()
            q.append((x, y))            
            while q:                
                x, y = q.popleft()                     
                for r, c in dir:
                    r += x
                    c += y
                    if ((r >= 0 and r < ROWS and c >= 0 and c < COLS) and 
                        (r, c) not in visit and board[r][c] == 'O'):
                        q.append((r, c)) 
                        visit.add((r, c))
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i == 0 or i == ROWS -1 or j == 0 or j == COLS - 1):
                    if (board[i][j] == 'O' and (i, j) not in visit):
                        # print(i,j)
                        bfs(i, j)
                        visit.add((i, j))
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visit:
                    board[i][j] = 'X'