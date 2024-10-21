class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        counter = 0

        for number in range(low, high + 1):
            str_num = str(number)
            length = len(str_num)
            
            if length % 2 == 0:
                mid = length // 2
                first_half = str_num[:mid]
                second_half = str_num[mid:]
                
                if sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half):
                    counter += 1

        return counter