class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        summ = 0

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if (j - i + 1) % 2 != 0:
                    summ += sum(arr[i:j+1])
        
        return summ