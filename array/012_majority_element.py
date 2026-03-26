"""
Problem: Majortiy Element
Platform: LeetCode
Link: https://leetcode.com/problems/majority-element/

Description:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = 0
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else:
                count -= 1

        return candidate
    
obj = Solution()
nums = [1,1,2,2,2]
result = obj.majorityElement(nums)
print("Majority Number in an array is :", result)