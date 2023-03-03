class Solution:
    def isPalindrome(self, s: str) -> bool:     
        if len(s.strip()) == 0:
            return True
        
        l, r = 0, len(s)-1        
        while l <= r:
            if not s[l].isalnum():
                while l < len(s) and not s[l].isalnum():
                    l += 1
            if not s[r].isalnum():
                while r >= 0 and not s[r].isalnum():
                    r -= 1                  
            if l > r:
                break
            if s[l].lower() != s[r].lower():
                return
            l += 1
            r -= 1
            
        return True
         