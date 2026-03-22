"""
Problem: Remove Element From Array
Platform: LeetCode
Link: https://leetcode.com/problems/remove-element/description/

Description: 
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
    

obj = Solution()
nums = [4,2,1,3,7,4,2,2]
result = obj.removeElement(nums, 4)

print("Number of elements are after removing the element 'val' from the array is : ", result)
print("Updated array : ", nums[:result])