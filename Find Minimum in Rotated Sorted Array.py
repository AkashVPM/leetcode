import math

class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) <= 1: 
            return nums[0]

        l = 0
        r = len(nums)-1

        out = math.inf

        while l < r: 
            check = (l+r) // 2

            if nums[check] > nums[r]: 
                out = min(out, nums[check+1])
                l = check + 1

            else: 
                out = min(out, nums[check])
                r = check

        return out