class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    counter += 1
        
        return counter