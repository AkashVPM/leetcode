class Solution:
    def strStr_worstcase(self, haystack: str, needle: str) -> int:
        
        if needle in haystack:
            return (haystack.index(needle))
        else: 
            return -1

    def strStr_good(self, haystack: str, needle: str) -> int:
        
        if needle in haystack:
            return (haystack.index(needle))
        else: 
            return -1