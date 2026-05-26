class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        total = 0
        l = 0   

        for i in range(len(nums)):

            if nums[i] == target: 
                return 1

            total += nums[i]

            while total >= target: 
                min_len = min(min_len, i-l+1) 
                total -= nums[l]
                l += 1

        return 0 if min_len == float('inf') else min_len