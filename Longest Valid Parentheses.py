class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        seen =  [-1]

        if s is None: 
            return longest 

        pairs = ')'

        for i in range(len(s)): 
            if s[i] in "(": 
                seen.append(i)
            else: 
                seen.pop() 
                if not seen: 
                    seen.append(i) 
                else:
                    longest = max(longest, i - seen[-1])
    
        return longest