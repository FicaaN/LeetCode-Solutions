class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rightStrip = s.rstrip()
        words = rightStrip.split(" ")

        return len(words[-1])