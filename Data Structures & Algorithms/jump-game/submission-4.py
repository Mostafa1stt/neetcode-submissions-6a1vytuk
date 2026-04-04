class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        i = 0
        while i < len(nums):
            if i + nums[i] >= len(nums) - 1:
                return True
            
            old = i
            for j in range(i + 1, i + nums[i] + 1):
                if nums[j] >= nums[i] - (j - i): 
                    i = j
                    break
            
            if i == old:
                return False
        
        return True