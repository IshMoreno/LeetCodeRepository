# Given integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1: nums = [1,2,3,1]
#   Output: True
# Example 2: nums = [1,2,3,4]
#   Output: False

class Solution:
  def hasDuplicate(self, nums: List[int]) -> bool:
    hashset() = set()

    for i in nums:
      if i in hashset():
        return True
      hashset.add(i)
    return False