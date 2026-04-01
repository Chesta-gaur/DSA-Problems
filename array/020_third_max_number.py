"""
Problem: Third Maximum Number
Platform: LeetCode
Link: https://leetcode.com/problems/third-maximum-number/

Description :
Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        unique_nums = set(nums)

        if len(unique_nums) < 3:
            return max(unique_nums)

        unique_nums.remove(max(unique_nums))
        unique_nums.remove(max(unique_nums))
        
        return max(unique_nums)
    
obj = Solution()
nums = [1,2,5,8,10,55]
result = obj.thirdMax(nums)
print("Third Maximum Number :", result)