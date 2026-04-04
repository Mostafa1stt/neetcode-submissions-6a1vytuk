class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i,v in enumerate(nums):
            multi = 1
            for j,l in enumerate(nums):
                if j == i:
                    continue
                multi *=l 
            res.append(multi)
        return res
            
        