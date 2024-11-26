class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        placements = []
        rankings = {}

        sorted_scores = sorted(score, reverse=True)

        for i, s in enumerate(sorted_scores):
            rankings[s] = i + 1
        
        for s in score:
            if rankings[s] == 1:
                placements.append("Gold Medal")
            elif rankings[s] == 2:
                placements.append("Silver Medal")
            elif rankings[s] == 3:
                placements.append("Bronze Medal")
            else:
                placements.append(str(rankings[s]))
        
        return placements