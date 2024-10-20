class Solution:
    def minElement(self, nums: List[int]) -> int:
        new_nums = [sum(int(digit) for digit in str(number)) for number in nums]

        return min(new_nums)