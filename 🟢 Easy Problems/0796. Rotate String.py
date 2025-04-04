class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        
        new_goal = goal + goal

        return s in new_goal