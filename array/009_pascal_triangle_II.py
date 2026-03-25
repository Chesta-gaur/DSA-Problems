"""
Problem: Pascal's Triangle 2nd Problem 
Platform: LeetCode
Link: https://leetcode.com/problems/pascals-triangle-ii/

Description:
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it

Constraints:
0 <= rowIndex <= 33
"""

class Solution:
    def pascalTriangle(self, rowIndex: int) -> list[int]:
        result = []
        for i in range(rowIndex+1):
            row = []
            for j in range(i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(result[i-1][j-1] + result[i-1][j])

            result.append(row)

        return result[rowIndex]
    
obj = Solution()
rowIndex = 3
lastRowOfTriangle = obj.pascalTriangle(rowIndex)
print("Last row elements of pascal's triangle : ", lastRowOfTriangle)
