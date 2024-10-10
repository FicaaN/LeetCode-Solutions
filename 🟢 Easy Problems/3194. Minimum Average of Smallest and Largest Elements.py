class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()

        while nums:
            maxElement = nums.pop(0)
            minElement = nums.pop(-1)
            avrg = (maxElement + minElement) / 2
            averages.append(avrg)
        
        return min(averages)