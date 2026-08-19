# ──────────────────────────────────────────────────
# Problem  : 67. Add Binary
# Difficulty: Easy
# Tags     : Math, String, Bit Manipulation, Simulation
# Link     : https://leetcode.com/problems/add-binary/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12292000 (beats 93%)
# Language : python
# Copyright: (c) 2026 mithunthangaraj06. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]   