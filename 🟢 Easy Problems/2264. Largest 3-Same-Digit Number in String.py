class Solution:
    def largestGoodInteger(self, num: str) -> str:
        digit = -1

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                digit = max(int(digit), int(num[i]))
        
        if digit != -1:
            return str(digit) * 3
        else: return ""