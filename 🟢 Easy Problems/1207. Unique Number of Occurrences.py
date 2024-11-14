class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_occ = set()
        counter = Counter(arr)

        for key, value in counter.items():
            if value in unique_occ:
                return False
            else:
                unique_occ.add(value)
                
        return True