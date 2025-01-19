class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        counter = 0
        for i in range(left, right + 1):
            set_bits = bin(i).count('1')
            if is_prime(set_bits):
                counter += 1
        
        return counter