class Solution:
    def countEven(self, num: int) -> int:
        counter = 0

        for number in range(1, num + 1):
            digits = [int(digit) for digit in str(number)]
            if sum(digits) % 2 == 0:
                counter += 1
                
        return counter