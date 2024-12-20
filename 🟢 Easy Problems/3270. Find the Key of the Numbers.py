class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        def leading_zeros(x: int) -> str:
            return str(x).zfill(4)
        
        key = ""
        num1 = leading_zeros(num1)
        num2 = leading_zeros(num2)
        num3 = leading_zeros(num3)

        for digits in zip(num1, num2, num3):
            min_digit = min(int(digits[0]), int(digits[1]), int(digits[2]))
            key += str(min_digit)
        
        return int(key)