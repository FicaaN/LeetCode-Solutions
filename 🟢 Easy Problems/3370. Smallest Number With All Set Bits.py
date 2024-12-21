class Solution:
    def smallestNumber(self, n: int) -> int:
        x = bin(n)[2:]
        x = "1" * len(x)
        return int(x, 2)