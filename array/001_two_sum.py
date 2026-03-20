"""
Problem: Two Sum
Platform: LeetCode
Link: https://leetcode.com/problems/two-sum/

Description: Given an array of integers nums and an integer target, 
             return indices of the two numbers such that they add up to target.
             You may assume that each input would have exactly one solution, 
             and you may not use the same element twice.

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109

"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j] 
        return []
    

# object
obj = Solution()

# call method
result = obj.twoSum([4,-2,5,0,6,3,2,7], 1)
print("indices of two numbers whose sum is 1 : ", result)