class Solution:
    def isValid(self, s: str) -> bool:
        stack = [-1]
        lpar = ['(', '{', '[']
        
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if c == ')' and stack[-1] == '(':
                    stack.pop()                    
                elif c == '}' and stack[-1] == '{':
                    stack.pop()                
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 1 else False 
                
        