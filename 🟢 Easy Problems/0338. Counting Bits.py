class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n + 1):
            count = str(bin(i)[2:]).count("1")
            output.append(int(count))
        
        return output