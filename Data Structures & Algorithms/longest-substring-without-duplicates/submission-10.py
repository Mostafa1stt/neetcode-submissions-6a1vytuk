class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        counters = []
        j = i = 0
        while j < len(s):
            if s[j] in cur:
                counters.append(len(s[i:j]))
                i+=1
                j=i
                cur = {s[j]}
            else:
                cur.add(s[j])
            j+=1
        counters.append(len(s[i:j]))
        return max(counters)