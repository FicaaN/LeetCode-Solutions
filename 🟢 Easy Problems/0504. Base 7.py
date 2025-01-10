class Solution:
    def convertToBase7(self, num: int) -> str:
        output = []
        sign_flag = False

        if num == 0:
            return "0"

        if num < 0:
            num = abs(num)
            sign_flag = True
        
        while num > 0:
            output.append(str(num % 7))
            num //= 7
        
        if sign_flag:
            return "-" + "".join(output[::-1])
        else:
            return "".join(output[::-1])