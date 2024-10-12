class Solution:
    def countAsterisks(self, s: str) -> int:
        counter = 0
        inside_bar = 0

        for char in s:
            if char == "|":
                inside_bar += 1
            
            if inside_bar % 2 == 0 and char == "*":
                counter += 1
        
        return counter