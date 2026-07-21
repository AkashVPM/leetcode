import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))
      
    def mySqrt_Binary_search(self, x: int) -> int:

        if x < 2: return x 

        out = 0
        
        left = 0 
        right = x 

        while left <= right: 
            mid = (left + right) // 2
            if mid * mid == x: 
                return int(mid)
            elif mid * mid < x:
                out = mid  
                left = mid + 1
            else: 
                right = mid -1
        
        return int(out) 
