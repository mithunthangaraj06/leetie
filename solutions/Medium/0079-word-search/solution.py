# ──────────────────────────────────────────────────
# Problem  : 79. Word Search
# Difficulty: Medium
# Tags     : Array, String, Backtracking, Depth-First Search, Matrix
# Link     : https://leetcode.com/problems/word-search/
# Runtime  : 5763 ms (beats 65%)
# Memory   : 11956000 (beats 99%)
# Language : python
# Copyright: (c) 2026 mithunthangaraj06. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or board[r][c] != word[i]
            ):
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            board[r][c] = temp
            return found

        for r in xrange(ROWS):
            for c in xrange(COLS):
                if dfs(r, c, 0):
                    return True

        return False