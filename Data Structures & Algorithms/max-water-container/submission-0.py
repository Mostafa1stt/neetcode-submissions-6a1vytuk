class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxium = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if heights[i] > heights[j]:
                    if ((j-i)*(heights[j])) > maxium:
                        maxium = ((j-i)*(heights[j]))
                else:
                    if ((j-i)*(heights[i])) > maxium:
                        maxium = ((j-i)*(heights[i]))
        return maxium


        