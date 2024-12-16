class Solution:
    def splitNum(self, num: int) -> int:
        num1, num2 = "", ""
        str_num = list(str(num))
        str_num.sort()
        sorted_num = "".join(str_num)

        for i in range(len(str_num)):
            if i % 2 == 0:
                num1 = num1 + str_num[i]
            else:
                num2 = num2 + str_num[i]

        output = int(num1) + int(num2)

        return output 