class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = ""
        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            output += chr(remainder + ord("A"))
            columnNumber = (columnNumber - 1) // 26
        
        return output[::-1]