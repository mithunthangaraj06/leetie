# ──────────────────────────────────────────────────
# Problem  : 3471. Find the Largest Almost Missing Integer
# Difficulty: Easy
# Tags     : Array, Hash Table
# Link     : https://leetcode.com/problems/find-the-largest-almost-missing-integer/
# Runtime  : 5 ms (beats 67%)
# Memory   : 12356000 (beats 52%)
# Language : python
# Copyright: (c) 2026 mithunthangaraj06. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter

class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        counts = Counter(nums)
        
        # Case 1: k == n
        if k == n:
            return max(nums)
        
        # Case 2: k == 1
        if k == 1:
            ans = -1
            for num, freq in counts.items():
                if freq == 1:
                    ans = max(ans, num)
            return ans
        
        # Case 3: 1 < k < n
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans