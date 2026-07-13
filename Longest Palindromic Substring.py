class Solution:
    def longestPalindrome(self, s: str) -> str:

        if s == None or len(s) <= 1: return s

        max_len = 0
        string = ''
        i = -1
        j = 0

        for i in range(len(s)): 
            l,r = i,i

            while (l >= 0 and r < len(s)) and s[l] == s[r]: 
                l -= 1 
                r += 1
            
            if r-l-1 > max_len: 
                max_len = r-l-1
                string = s[l+1:r]
        
            l = i
            r = i+1

            while (l >= 0 and r < len(s)) and s[l] == s[r] : 
                l -= 1
                r += 1

            if r-l-1 > max_len: 
                max_len = r-l-1
                string = s[l+1:r]
        
        return string