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

def merge_sort_sorted_array(nums_1:list , nums_2:list): 
      l = 0
      r = 0

      new_list = []

      while l < len(nums_1) and r < len(nums_2): 
            while l < len(nums_1) and nums_1[l] < nums_2[r]: 
                  new_list.append(nums_1[l])
                  l += 1

            while r < len(nums_2) and nums_1[l] >= nums_2[r]: 
                  new_list.append(nums_2[r])
                  r += 1
      
      new_list.extend(nums_1[l:])
      new_list.extend(nums_2[r:])
      
      return new_list
            


# a = [2,0,2,1,1,0]
# print(intersection_sort(a))

a = [17,29,32,38]
b = [2,5,21,35]

# print(merge_sort(a,b))