"""
Problem: Pascal's Triangle Problem
Platform: LeetCode
Link: https://leetcode.com/problems/pascals-triangle/

Description:
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Constraints:
1 <= numRows <= 30
"""

class Solution:
    def pascalTriangle(self, numRows: int) -> list[list[int]]:
        result = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(result[i-1][j-1] + result[i-1][j])

            result.append(row)

        return result
    
obj = Solution()
numRows = 5
pascalTriangleArray = obj.pascalTriangle(numRows)

print(f"Pascal Triangle Array of {numRows} rows : ", pascalTriangleArray)