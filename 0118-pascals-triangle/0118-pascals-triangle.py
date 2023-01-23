class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        pas = [[1] for i in range(numRows)]
        pas[1].append(1)        
        
        for i in range(1, numRows - 1):
            for j in range(len(pas[i])-1):
                pas[i+1].append(pas[i][j] + pas[i][j+1]) 
            pas[i+1].append(1)
            
        return(pas)
                
            