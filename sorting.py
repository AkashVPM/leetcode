def bubble_sort(self, nums: list[int]) -> None:
      "Move the Bigger to the end of the list"
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
      "Move the smaller number to the begining of the list"
      for i in range(len(nums)): 
            j = i
            while j > 0 and nums[j-1] > nums[j]: 
                  nums[j], nums[j-1] = nums[j-1], nums[j]
                  if j < len(nums):
                        j -= 1
      
      return nums

def merge_sort_sorted_array(nums_1:list , nums_2:list): 

      # print(nums_1, nums_2)
      l = 0
      r = 0

      new_list = []

      while l < len(nums_1) and r < len(nums_2): 
            if l < len(nums_1) and nums_1[l] < nums_2[r]: 
                  new_list.append(nums_1[l])
                  l += 1

            elif r < len(nums_2) and nums_1[l] >= nums_2[r]: 
                  new_list.append(nums_2[r])
                  r += 1
      
      new_list.extend(nums_1[l:])
      new_list.extend(nums_2[r:])
      
      return new_list
            
def merge_sort_unsorted_array(nums: list[int]) -> list: 
      if len(nums) <= 1: 
            return nums
      
      mid = len(nums) // 2
      left  = nums[:mid]
      right = nums[mid:]

      if left: 
            left_sort = merge_sort_unsorted_array(left)
      if right: 
            right_sort = merge_sort_unsorted_array(right)

      return merge_sort_sorted_array(left_sort,right_sort)

def shell_sort(nums): 
      if len(nums) < 2: 
            return nums
      
      # nums = nums
      length = len(nums)
      gap = len(nums) //2

      while gap:
            for i in range(gap,length): 
                  check = nums[i]

                  j = i 

                  while j >= gap and nums[j-gap] > check: 
                        nums[j] = nums[j-gap]
                        j -= gap
                  
                  nums[j] = check
            gap = gap // 2
      
      return nums





# a = [2,0,2,1,1,0]
# print(intersection_sort(a))

a = [100,17,29,32,38,50,52,80,0,1,2,0]
b = [2,5,21,35,1]

# c = a+b 
# print(merge_sort_unsorted_array(c))
print(shell_sort(a))
# print(merge_sort_sorted_array(a,b))