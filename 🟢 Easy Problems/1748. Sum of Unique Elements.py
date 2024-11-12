class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        summ = 0
        counter = Counter(nums)

        for key, value in counter.items():
            if value == 1:
                summ += key
        
        return summ