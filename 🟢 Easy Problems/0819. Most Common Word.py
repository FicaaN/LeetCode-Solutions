class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counter = Counter()
        punctuations = list(string.punctuation)

        paragraph = paragraph.lower()

        for p in punctuations:
            paragraph = paragraph.replace(p, " ")
        
        paragraph_words = paragraph.split()

        for word in paragraph_words:
            if word not in banned:
                counter[word] += 1
        
        output = max(counter, key=counter.get)

        return output