class Solution:
    def canJump(self, nums: List[int]) -> bool:
        checker = 0
        i=0
        old = i
        if len(nums)==1:
            return True
        while i<len(nums):
            old = i
            checker = nums[i]
            for j in range(i+1,i+ nums[i]+1):
                if i+nums[i]+1 >= len(nums):
                    return True
                if checker  <= nums[j]:
                    i = j
                    break
                checker -=1
            if i==old:
                return False
        return True