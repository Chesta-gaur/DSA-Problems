"""
Problem: Intersection Of Two Array 2
Platform: LeetCode
Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Description:
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq = Counter(nums1)
        result = []

        for num in nums2:
            if freq[num] > 0:
                result.append(num)
                freq[num] -= 1

        return result
    
obj = Solution()
nums1 = [1,2,2,3]
nums2 = [2,2]
sol = obj.intersect(nums1, nums2)
print(sol)