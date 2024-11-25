class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        chars_count = Counter(words[0])

        for word in words[1:]:
            chars_count &= Counter(word)
        
        for char, count in chars_count.items():
            result.extend([char] * count)
        
        return result