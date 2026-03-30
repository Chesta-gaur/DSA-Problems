"""
Problem: Intersection Of Two Arrays
Platform: LeetCode
Link: https://leetcode.com/problems/intersection-of-two-arrays/

Description:
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

class Solution:
    def intersectionOfArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        set1 = set(arr1)
        resultant_array = set()

        for num in arr2:
            if num in set1:
                resultant_array.add(num)

        return list(resultant_array)
    
obj =  Solution()
arr1 = [2,1,4,5]
arr2 = [5,1,9,7]
result = obj.intersectionOfArray(arr1, arr2)
print("Updated array after intersection of two arrays :",result)