"""
Problem: Set Mistmatch
Platform: LeetCode
Link: https://leetcode.com/problems/set-mismatch/

Description:
You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another 
number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Constraints:
2 <= nums.length <= 104
1 <= nums[i] <= 104
"""

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        num_set = set()
        duplicate = -1
        
        for num in nums:
            if num in num_set:
                duplicate = num
            num_set.add(num)
        
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        
        missing = expected_sum - (actual_sum - duplicate)
        
        return [duplicate, missing]
    

obj = Solution()
nums = [1,2,2,4]
result = obj.findErrorNums(nums)
print("Number that occurs twice and number that is missing :", result)