class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lSum = [0] * n
        rSum = [0] * n
        output = [0] * n

        for i in range(1, n):
            lSum[i] = lSum[i - 1] + nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            rSum[i] = rSum[i + 1] + nums[i + 1]
        
        for i in range(n):
            output[i] = abs(lSum[i] - rSum[i])
        
        return output