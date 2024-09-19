# Given twp strings s and t, return true if the two strings are anagrams of each other, and false otherwise.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1: s = "anagram", t = "nagaram"
#   Output: True
# Example 2: s = "rat", t = "car"
#   Output: False

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    countS = {}
    countT = {}

    for i in range(len(s)):
      countS[s[i]] = countS.get(s[i], 0) + 1
      countT[t[i]] = countT.get(t[i], 0) + 1

    return countS == countT

# Time Complexity: O(n)
# Space Complexity: O(n)