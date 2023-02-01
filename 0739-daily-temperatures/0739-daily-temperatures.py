class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stack = []
        stack.append((temp[0], 0))
        i = 1
        while i < len(temp):            
            if stack and temp[i] > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop() 
            else:
                stack.append((temp[i], i))
                i += 1            
        return res
                
                