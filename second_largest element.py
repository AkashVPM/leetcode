class Solution: 
      def second_largest_elem(nums:list[int]) -> int:
            large = float('-inf')
            second_large = float('-inf')

            for num in nums:
                  if num > large: 
                        second_large = large
                        large = num
                  elif num > second_large and num < large: 
                        second_large = num

            return second_large
