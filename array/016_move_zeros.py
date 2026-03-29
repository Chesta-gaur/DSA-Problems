"""
Problem: Move Zeros
Platform: LeetCode
Link: https://leetcode.com/problems/move-zeroes/

Description:
Given an integer array nums, move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

class Solution:
    def moveZeros(self, nums: list[int]) -> list[int]:
        k = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        for i in range(k, len(nums)):
            nums[i] = 0

        return nums
    

obj = Solution()
nums = [0,1,0,3,12]
result = obj.moveZeros(nums)
print("Updated array after moving zeros at the end :", result)