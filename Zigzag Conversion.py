class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == None or len(s) == 1 or numRows == 1: return s
        
        out = ''
        new_len = numRows
        cycle = (new_len - 1)*2

        for i in range(numRows):
            l = i
            count = 0
            while l <= len(s)-1: 
                out += s[l]
                if i == 0 or i == numRows-1:
                    l += cycle
                else: 
                    if count % 2 == 0:
                        l += cycle - 2*i 
                    if count % 2 != 0: 
                        l += 2*i
                    count += 1 

        return out
            