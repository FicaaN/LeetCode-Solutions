class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        output = 0
        
        for i in range(len(nums)):
            if format(i, "b").count("1") == k:
                output += nums[i]
        
        return output