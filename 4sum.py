class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        out = set()

        nums.sort()

        for a in range(len(nums)-3): 
            if a > 0 and nums[a] == nums[a-1]: continue

            for b in range(a+1, len(nums)-2): 
                if b > a+1 and nums[b] == nums[b-1]: continue
                    
                c = b + 1
                d = len(nums) - 1

                while c < d: 
                    val = nums[a] + nums[b] + nums[c] + nums[d]

                    if val == target: 
                        out.add((nums[a], nums[b],nums[c],nums[d]))
                        c += 1
                        d -= 1 
                    
                    elif val < target: 
                        c += 1
                    
                    elif val > target: 
                        d -= 1

        return [list(i) for i in out]
