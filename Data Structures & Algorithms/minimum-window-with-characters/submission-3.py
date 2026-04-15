class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = dict()
        for x in t:
            c[x] = c.get(x,0) + 1
        r = c.copy()
        n = 0
        i = -1
        j=0
        output = []
        while j < len(s):
            print(i,j,n,c)
            if s[j] in t and i == -1:
                i = j
                c[s[j]] -= 1
            elif s[j] in t and c[s[j]] > 0 and n == 0:
                n = j
                c[s[j]] -= 1
            elif s[j] in t and c[s[j]] > 0:
                c[s[j]] -= 1

            elif s[j] in t and c[s[j]] <= 0 and n == 0:
                n = j

            if max(c.values()) == 0:
                output.append(s[i:j+1])
                c = r.copy()
                if n == 0:
                    break
                i = -1
                j = n-1
                n = 0
            j += 1
        if output:
            return min(output, key=len)
        else:
            return ""