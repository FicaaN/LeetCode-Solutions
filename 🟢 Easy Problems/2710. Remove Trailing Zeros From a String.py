class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        new_num = num.rstrip("0")

        return new_num