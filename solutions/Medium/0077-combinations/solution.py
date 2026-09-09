# ──────────────────────────────────────────────────
# Problem  : 77. Combinations
# Difficulty: Medium
# Tags     : Backtracking
# Link     : https://leetcode.com/problems/combinations/
# Runtime  : 179 ms (beats 92%)
# Memory   : 139552000 (beats 15%)
# Language : python
# Copyright: (c) 2026 mithunthangaraj06. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

  def combine(self, n, k):
    res = []

    def backtrack(start, path):
      if len(path) == k:
        res.append(list(path))
        return

      for i in range(start, n - (k - len(path)) + 2):
        path.append(i)
        backtrack(i + 1, path)
        path.pop()

    backtrack(1, [])
    return res   