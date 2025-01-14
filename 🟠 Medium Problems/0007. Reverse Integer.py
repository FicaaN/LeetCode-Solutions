class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            reversed_x = int(str(x)[::-1])
        else:
            reversed_x = -1 * int(str(abs(x))[::-1])
        
        if reversed_x > 2 ** 31 - 1 or reversed_x < -2 ** 31:
            return 0
        
        return reversed_x
