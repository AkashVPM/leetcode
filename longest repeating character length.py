class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        max_len  = 0
        dummy_dict = {}

        for r in range(len(s)): 
            if s[r] not in dummy_dict: # creaeting dict to store the number of characters
                dummy_dict[s[r]] = 1
            else: dummy_dict[s[r]] += 1

            if (r-l+1) - max(dummy_dict.values()) > k:
                dummy_dict[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)