class Solution:
    def convertDateToBinary(self, date: str) -> str:
        output = []

        parts = date.split("-")

        for part in parts:
            output.append(format(int(part), "b"))
            
        return "-".join(output)

        # Can be done with one liner
        # return "-".join(format(int(part), 'b') for part in date.split("-"))