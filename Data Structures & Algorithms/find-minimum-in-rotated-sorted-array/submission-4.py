class Solution:
    def cutter(self,array,l,r):

        if array[l] < array[r-1]:
            return array[l]

        if len(array[l:r])<2:
            return array[l]
                   
        m = (r+l)//2
        return min(self.cutter(array,l,m),self.cutter(array,m,r))

    def findMin(self, nums: List[int]) -> int:
        return self.cutter(nums,0,len(nums))        