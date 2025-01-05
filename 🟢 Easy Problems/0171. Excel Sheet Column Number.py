class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0
        for char in columnTitle:
            output = output * 26 + (ord(char) - ord("A") + 1)
        
        return output