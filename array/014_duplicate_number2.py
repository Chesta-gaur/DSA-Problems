"""
Problem: Duplicate Number 2
Platform: LeetCode
Link: https://leetcode.com/problems/contains-duplicate-ii/

Description:
Given an integer array nums and an integer k, return true if there are two distinct indices
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True

            seen[nums[i]] = i

        return False

obj = Solution()
nums = [1,2,3,1]
k = 3

result = obj.containsNearbyDuplicate(nums, k)
print(result)