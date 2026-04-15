class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        j = i = 0
        cur = s[0]
        counter = 0
        res = 0
        r = k
        while j<len(s):
            if s[j] == cur :
                counter += 1
                j += 1
            else:
                if k==r:
                    i=j
                if k>0:
                    k -= 1
                    j += 1
                    counter += 1
                else:
                    res = max(counter,res)
                    j = i 
                    cur = s[j]
                    counter = 0
                    k = r   
            if j >= len(s):
                res = max(counter + min(len(s)-counter,k),res)
                if (j-i) != counter:
                    j = i
                    cur = s[j]
                    counter = 0
                    k = r   
        return res
