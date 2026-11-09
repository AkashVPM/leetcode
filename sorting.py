def bubble_sort(self, nums: list[int]) -> None:
      """
      Do not return anything, modify nums in-place instead.
      """
      
      for i in range(len(nums)-1):
            sorting = False
            for j in  range(len(nums)-1):
                  if nums[j] > nums[j+1]: 
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        sorting = True
                  
            if not sorting: 
                  continue

def intersection_sort(nums):
      for i in range(len(nums)): 
            j = i
            while j > 0 and nums[j-1] > nums[j]: 
                  nums[j], nums[j-1] = nums[j-1], nums[j]
                  if j < len(nums):
                        j -= 1
      
      return nums

a = [2,0,2,1,1,0]
print(intersection_sort(a))