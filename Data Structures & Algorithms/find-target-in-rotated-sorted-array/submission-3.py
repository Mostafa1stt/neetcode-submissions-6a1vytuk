class Solution:
    def cutter(self, array, l, r,target):
        if r-l==0:
            return -1
        if r-l ==1:
            if array[l] == target:
                return l
            else:
                return -1

        m = (l+r) // 2
        if array[l] < array[r-1]:
            if array[m] == target:
                return m
            elif array[m] < target:
                return self.cutter(array,m+1,r,target)
            else:
                return self.cutter(array,l,m,target)
        else:
            return max(self.cutter(array,l,m,target),self.cutter(array,m,r,target))
        

    def search(self, nums: List[int], target: int) -> int:
        return self.cutter(nums,0,len(nums),target)
        