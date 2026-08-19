# ──────────────────────────────────────────────────
# Problem  : 1386. Cinema Seat Allocation
# Difficulty: Medium
# Tags     : Array, Hash Table, Greedy, Bit Manipulation
# Link     : https://leetcode.com/problems/cinema-seat-allocation/
# Runtime  : 23 ms (beats 99%)
# Memory   : 15864000 (beats 96%)
# Language : python
# Copyright: (c) 2026 mithunthangaraj06. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        seats = defaultdict(int)
        for row, seat in reservedSeats:
            seats[row] |= (1 << (seat - 1))
            
        ans = (n - len(seats)) * 2
        
        for mask in seats.values():
            left = not (mask & 0b0111100000)
            right = not (mask & 0b0000011110)
            mid = not (mask & 0b0001111000)
            
            if left and right:
                ans += 2
            elif left or right or mid:
                ans += 1
                
        return ans