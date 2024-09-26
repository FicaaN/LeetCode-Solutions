class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_sum = 0

        for r in range(len(nums) + 1):
            for subset in combinations(nums, r):
                xor_total = 0
                for num in subset:
                    xor_total ^= num
                total_sum += xor_total

        return total_sum