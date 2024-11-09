class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        
        max_value = 0
        max_key = 0

        for key, value in counts.items():
            if value > max_value:
                max_value = value
                max_key = key
        
        return max_key