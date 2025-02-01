class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        flag = True
        if n == 1:
            return True

        for i in range(n - 1):
            if (nums[i] + nums[i + 1]) % 2 != 0:
                continue
            else:
                flag = False
                break
        
        return flag