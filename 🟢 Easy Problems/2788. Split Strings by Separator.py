class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        splitted_words = []

        for word in words:
            sep_words = word.split(separator)
            filtered_words = [word for word in sep_words if word != ""]
            splitted_words.extend(filtered_words)
        
        return splitted_words