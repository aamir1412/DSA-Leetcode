class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:        
        ROWS, COLS = len(board), len(board[0])    
        visit = set() 
        flag = [False]
        
        def dfs(x, y, idx):
            if idx == len(word):
                flag[0] = True
                return 
            if x < 0 or x >= ROWS or y < 0 or y >= COLS:
                return
            if board[x][y] != word[idx] or (x, y) in visit:
                return
            
            visit.add((x, y))
            dfs(x + 1, y, idx+1)  
            dfs(x, y + 1, idx+1)  
            dfs(x - 1, y, idx+1)  
            dfs(x, y - 1, idx+1)  
            visit.remove((x, y))
                              
        for i in range(ROWS):
            for j in range(COLS):                 
                if board[i][j] == word[0]:
                    dfs(i, j, 0)
                    if flag[0]:
                        return True
                        
        
        