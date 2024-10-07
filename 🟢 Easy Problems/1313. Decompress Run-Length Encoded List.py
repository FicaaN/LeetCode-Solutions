class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)

        for i in range(0, n, 2):
            freq = nums[i]
            val = nums[i + 1]
            output.extend([val] * freq)

        return output