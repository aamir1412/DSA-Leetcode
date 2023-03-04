class Solution:
    def isValid(self, s: str) -> bool:
        lpar = ('(', '{', '[')
        stack = [-99]
        
        for c in s:
            if c in lpar:
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
        return len(stack) == 1
                    
                    
        