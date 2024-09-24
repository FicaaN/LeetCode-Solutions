class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        output = []
        nums1 = set()
        
        for number in nums:
            if number in nums1:
                output.append(number)
            else:
                nums1.add(number)
        
        return output