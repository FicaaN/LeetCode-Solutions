class Solution:
    def toHex(self, num: int) -> str:
        hexx = "0123456789abcdef"
        output = []

        if num == 0:
            return "0"

        if num < 0:
            num+= 2 ** 32
        
        if num > 0 and num <= 15:
            return hexx[num]
        
        while num > 0:
            output.append(hexx[num % 16])
            num //= 16

        return "".join(output[::-1])