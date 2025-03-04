class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        output = []
        counter = Counter()

        s = s1 + " " + s2
        new_s = s.split()

        for word in new_s:
            counter[word] += 1

        for key, value in counter.items():
            if value == 1:
                output.append(key)

        return output