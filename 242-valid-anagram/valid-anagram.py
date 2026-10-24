class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 2
        return sorted(s) == sorted(t)