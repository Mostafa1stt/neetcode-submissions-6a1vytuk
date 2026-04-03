class Solution:

    def anagram(self,string1 , string2):
        return(sorted(string1) == sorted(string2))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        output = []
        for i , v in enumerate(strs):
            if i in seen:
                continue
            anagrams = [v]
            seen.add(i)
            for j in range(i+1,len(strs)):
                if j not in seen and self.anagram(strs[j],v):
                    anagrams.append(strs[j])
                    seen.add(j)
            output.append(anagrams)
        return output
 