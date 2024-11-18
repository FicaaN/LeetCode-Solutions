class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        counter = 0

        for word in words:
            if not any(char in word for char in brokenLetters):
                counter += 1
        
        return counter