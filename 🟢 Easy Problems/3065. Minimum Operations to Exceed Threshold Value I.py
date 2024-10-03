class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        nums.sort()

        for number in nums:
            if number < k:
                counter += 1
        
        return counter
