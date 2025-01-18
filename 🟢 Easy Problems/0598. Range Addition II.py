class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row, min_column = m, n

        for row, column in ops:
            min_row, min_column = min(min_row, row), min(min_column, column)

        return min_row * min_column