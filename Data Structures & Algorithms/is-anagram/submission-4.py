class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = list(t)
        d.sort()
        a = list(s)
        a.sort()
        return d == a