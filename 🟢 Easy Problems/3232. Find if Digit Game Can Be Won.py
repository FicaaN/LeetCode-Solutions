class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit, double_digit = 0, 0
        for number in nums:
            if number < 10:
                single_digit += number
            else:
                double_digit += number
            
        return single_digit > double_digit or double_digit > single_digit