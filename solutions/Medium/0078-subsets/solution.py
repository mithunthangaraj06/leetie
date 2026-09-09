# ──────────────────────────────────────────────────
# Problem  : 78. Subsets
# Difficulty: Medium
# Tags     : Array, Backtracking, Bit Manipulation
# Link     : https://leetcode.com/problems/subsets/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12624000 (beats 25%)
# Language : python
# Copyright: (c) 2026 mithunthangaraj06. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

  def subsets(self, nums):
    res = []

    def backtrack(index, path):
      res.append(list(path))
      for i in range(index, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()

    backtrack(0, [])
    return res