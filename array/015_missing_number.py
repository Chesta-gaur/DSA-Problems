"""
Problem: Missing Number
Platform: LeetCode
Link: https://leetcode.com/problems/missing-number/

Description:
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        xor = 0
        n = len(nums)

        for i in range(n + 1):
            xor ^= i

        for num in nums:
            xor ^= num

        return xor
    
obj = Solution()
nums = [3,0,2,1,5,6]
result = obj.missingNumber(nums)
print("Missing value in the range :", result)