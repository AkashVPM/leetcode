class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}

        for i,num in enumerate(nums):
            remain = target - num

            if remain in seen: 
                return [seen[remain],i] 
            
            seen[num] = i
            
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        arr = [(ind, num) for num, ind in enumerate(nums)]
        arr.sort()

        l = 0
        r = len(arr)-1

        while l < r:
            if arr[r][0] + arr[l][0] == target: 
                out.append(arr[r][1])
                out.append(arr[l][1])
                break

            elif arr[r][0] + arr[l][0] < target:
                l += 1

            else: 
                r -= 1

        return out 