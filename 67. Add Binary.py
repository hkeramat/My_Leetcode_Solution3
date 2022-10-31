class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = a[::-1]
        b = b[::-1]
        n = max(len(a), len(b))
        
        ans = ""
        carry = 0
        for i in range(n):
            
            if i < len(a):
                a_digit = ord(a[i]) - ord('0')
            else:
                a_digit = 0
                
            if i < len(b):
                b_digit = ord(b[i]) - ord('0')
            else:
                b_digit = 0
                
            total = a_digit + b_digit + carry
            new_digit = str(total % 2)
            
            ans =  new_digit + ans
            carry = total //2
        
        if carry:
            ans = str(carry )+ans
        
        return ans
