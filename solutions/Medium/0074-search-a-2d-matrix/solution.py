# ──────────────────────────────────────────────────
# Problem  : 74. Search a 2D Matrix
# Difficulty: Medium
# Tags     : Array, Binary Search, Matrix
# Link     : https://leetcode.com/problems/search-a-2d-matrix/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12252000 (beats 0%)
# Language : python
# Copyright: (c) 2026 mithunthangaraj06. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def searchMatrix(self, matrix, target):
        i = 0
        j = len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1

        return False