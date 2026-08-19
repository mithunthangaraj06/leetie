# ──────────────────────────────────────────────────
# Problem  : 69. Sqrt(x)
# Difficulty: Easy
# Tags     : Math, Binary Search, Newton's Method
# Link     : https://leetcode.com/problems/sqrtx/
# Runtime  : 7 ms (beats 28%)
# Memory   : 12272000 (beats 90%)
# Language : python
# Copyright: (c) 2026 mithunthangaraj06. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def mySqrt(self, x):
        left, right = 0, x
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans
        