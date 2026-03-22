"""
Problem: Search insert Position
Platform: LeetCode
Link: https://leetcode.com/problems/search-insert-position/

Description: 
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

class Solution:
    def searchInsertPosition(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return left
    

obj = Solution()
nums = [1,3,5,6]
# nums = [1,3,4,6,7]
result = obj.searchInsertPosition(nums, 5)

print("Index of target number : ", result)