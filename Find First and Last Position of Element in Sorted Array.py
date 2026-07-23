class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if nums == []: return [-1,-1]
        if len(nums) == 1: 
            if target in nums: 
                return [0,0]
            else: 
                return[-1,-1]

        out = []

        l = 0
        r = len(nums) - 1 

        while l < r: 
            check = (l+r) // 2

            if nums[check] == target: 
                c = check
                d = check

                while c >= 0 and nums[c] == target: 
                    c -= 1

                while d < len(nums) and nums[d] == target: 
                    d += 1

                return [c+1, d-1]
            
            elif nums[check] < target: 
                l = check + 1
            else:
                r = check - 1

        return out if out else [-1,-1]