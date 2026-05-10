"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merger_list = nums1 + nums2
        merged_list = sorted(merger_list)

        length = len(merged_list)

        if length % 2 == 0:
            middle1 = length // 2
            middle2 = middle1 - 1
            return (merged_list[middle1] + merged_list[middle2]) / 2

        if length % 2 != 0:
            middle1 = length // 2
            return merged_list[middle1]

    def findMedianSortedArraysPointer(self, nums1: List[int], nums2: List[int]) -> float:
        num1 = nums1 
        num2 = nums2
        m, n = len(num1), len(num2)
        prev = curr = 0 
        i = j = 0

        for k in range((m+n)//2+1):
            prev = curr
            if i < m and (j >= n or  num1[i] <= num2[j]): 
                curr = num1[i]
                i += 1
            else:
                curr = num2[j]
                j += 1

        if (m+n) % 2 == 0:
            return (prev + curr)/2
        return curr