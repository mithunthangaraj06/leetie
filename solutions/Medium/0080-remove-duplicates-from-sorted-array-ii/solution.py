# ──────────────────────────────────────────────────
# Problem  : 80. Remove Duplicates from Sorted Array II
# Difficulty: Medium
# Tags     : Array, Two Pointers
# Link     : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Runtime  : 69 ms (beats 63%)
# Memory   : 15256000 (beats 68%)
# Language : python
# Copyright: (c) 2026 mithunthangaraj06. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        k = 2
        for i in xrange(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k