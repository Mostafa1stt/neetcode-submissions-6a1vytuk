class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxium = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                curent =  min(heights[i] , heights[j]) * (j-i)
                if curent > maxium:
                    maxium = curent
        return maxium


        