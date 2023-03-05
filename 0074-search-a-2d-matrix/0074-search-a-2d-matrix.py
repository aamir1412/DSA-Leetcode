class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bs(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r)//2
                if arr[m] == target:
                    return True, [m, m]
                if arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False, [l, r]
        
        col = []
        for x in (matrix):
            col.append(x[0])
        
        flag, r = bs(col)
        r = min(r)
        if flag:
            return True
        
        flag, res = bs(matrix[r])        
        return flag
        