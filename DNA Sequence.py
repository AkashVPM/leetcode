class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeat = set()

        l = 0
        r = l + 10

        while r <= len(s): 
            check = s[l:r]

            if check in seen: 
                repeat.add(check)
            else: 
                seen.add(check)

            l += 1
            r += 1
        
        return list(repeat)