class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        output = []
        w = round(area ** 0.5)

        while True:
            l = area // w
            if (l * w) == area:
                output = [l, w]
                break
            else:
                w -= 1

        return output