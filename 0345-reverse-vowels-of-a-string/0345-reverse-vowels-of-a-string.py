class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = {'a','e','i','o','u', 'A','E','I','O','U'}
        res = list(s) 
        
        l = 0
        r = len(s) - 1                       
        while(l < r):
            if res[l] in vow and res[r] in vow:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
            if res[l] not in vow:
                l += 1
            if res[r] not in vow:
                r -= 1
                
        return ''.join(res)
        