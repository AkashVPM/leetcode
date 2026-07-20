class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        out = float('inf')
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r: 
                val = nums[i] + nums[l] + nums [r]
                diff = abs(val - target)

                if abs(out - target) > diff:
                    out = val

                if val < target: 
                    l += 1
                elif val > target:
                    r -= 1
                else:
                    return val
        
        return out

a = Solution()
res = a.threeSumClosest([-1,2,1,-4], 1)
print(res)

