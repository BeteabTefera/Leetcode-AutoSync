class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1

        if len(s) != len(t):
            return False

        dic_s = {i : s.count(i) for i in s}
        dic_t = {i : t.count(i) for i in t}

        return dic_s == dic_t