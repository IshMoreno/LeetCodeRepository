# Given integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1: nums = [1,2,3,1]
#   Output: True
# Example 2: nums = [1,2,3,4]
#   Output: False

from typing import List

my_list = [1, 2, 3, 1]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      hashset = set()

      for num in nums:
        if num in hashset:
          return True
        hashset.add(num)

      return False