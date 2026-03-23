"""
Problem: Merge Sorted Array
Platform: LeetCode
Link: https://leetcode.com/problems/merge-sorted-array/

Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored 
inside the array nums1. To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, and the last n elements are set to 0 
and should be ignored. nums2 has a length of n.

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""

class Solution:
    def mergeArray(self, arr1: list[int], m: int, arr2: list[int], n: int) -> list[int]:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if arr1[i] > arr2[j]:
                arr1[k] = arr1[i]
                i -= 1
            else:
                arr1[k] = arr2[j]
                j -= 1
            k -= 1

        while j >= 0:
            arr1[k] = arr2[j]
            j -= 1
            k -= 1


        return arr1

obj = Solution()
arr1 = [1, 2, 0, 0]
m = 2
arr2 = [2, 4] 
n = 2

result = obj.mergeArray(arr1, m, arr2, n)
print("updated array after merge : ",result)