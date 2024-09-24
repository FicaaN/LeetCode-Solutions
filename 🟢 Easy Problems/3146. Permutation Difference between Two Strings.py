class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        index_s = 0
        output = 0
        for char_s in s:
            for index_t, char_t in enumerate(t):
                if char_s == char_t:
                    output += abs(index_s - index_t)
            index_s += 1
        
        return output