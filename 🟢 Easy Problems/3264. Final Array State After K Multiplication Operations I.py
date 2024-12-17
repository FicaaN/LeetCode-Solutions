class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        def min_num(l: list) -> int:
            value = math.inf
            index = 0
            for i in range(len(l)):
                if l[i] < value:
                    value = l[i]
                    index = i
            return index
        
        index = 0

        while k != 0:
            index = min_num(nums)
            nums[index] *= multiplier
            k -= 1
        
        return nums