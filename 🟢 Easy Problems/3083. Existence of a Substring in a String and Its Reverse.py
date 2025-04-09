class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reversed_s = s[::-1]
        substring = ""

        for i in range(len(s) - 1):
            substring = s[i] + s[i + 1]
            if substring in reversed_s:
                return True
        
        return False