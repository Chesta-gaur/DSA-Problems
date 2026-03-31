"""
Problem: Convert Sorted Array To BST
Platform: LeetCode
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Description:
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        
        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums)-1)
    

def level_order(root):
    if not root:
        return
    
    q = deque([root])
    
    while q:
        node = q.popleft()
        
        if node:
            print(node.val, end=" ")
            q.append(node.left)
            q.append(node.right)
        else:
            print("null", end=" ")


nums = [-10, -3, 0, 5, 9]

sol = Solution()
root = sol.sortedArrayToBST(nums)
level_order(root)
