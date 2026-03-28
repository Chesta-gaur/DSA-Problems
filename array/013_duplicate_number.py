"""
Problem: Duplicate Number
Platform: LeetCode
Link: https://leetcode.com/problems/contains-duplicate/

Description:
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def duplicateNumber(self, nums: list[int]) -> bool:
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            
        return False
    
obj = Solution()
nums = [1,4,1,2,2,3]
result = obj.duplicateNumber(nums)
print(result)