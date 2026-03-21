"""
Problem: Longest Common Prefix
Platform: LeetCode
Link: https://leetcode.com/problems/two-sum/

Description: Write a function to find the longest common prefix string amongst an array of strings.
             If there is no common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
            
        return prefix
    
obj = Solution()
# result = obj.longestCommonPrefix(["meena", "meethi", "meetali"])
result = obj.longestCommonPrefix(["flower", "flow", "flight"])
print("Longest Common Prefix is : ", result)