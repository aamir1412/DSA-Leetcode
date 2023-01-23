class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        i, j = len(a)-1, len(b)-1
        carry = 0
        
        while (i >= 0 or j >= 0):
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0            
                              
            res += str(x ^ y ^ carry)
            if((x > 0 and y > 0) or (y > 0 and carry > 0) or (x > 0 and carry > 0)):
                carry = 1
            else:
                carry = 0
            i -= 1
            j -= 1
            
        if carry > 0:
            res += '1'
        return (res[::-1])
        
            
        
        