"""
Problem: Remove Duplicate Numbers From Array
Platform: LeetCode
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Description: Given an integer array nums sorted in non-decreasing order, 
             remove the duplicates in-place such that each unique element appears only once. 
             The relative order of the elements should be kept the same.
             Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, 
             return the number of unique elements k. The first k elements of nums should contain the 
             unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

class Solution:
    def removeDuplicateNums(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1

        return k
    

obj = Solution()
result = obj.removeDuplicateNums([1,1,2,2,3,4,5,6,6,7])
print("Unique number of elements in a list : ", result)