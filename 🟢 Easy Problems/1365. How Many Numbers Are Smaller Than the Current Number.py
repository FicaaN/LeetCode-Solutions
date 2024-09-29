class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        num_smaller = {}
        
        for i, num in enumerate(sorted_nums):
            if num not in num_smaller:
                num_smaller[num] = i

        return [num_smaller[num] for num in nums]