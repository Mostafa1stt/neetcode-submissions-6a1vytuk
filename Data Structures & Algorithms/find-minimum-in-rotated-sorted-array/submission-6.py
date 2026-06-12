class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        if not nums:
            return 0
        mid = len(nums)//2
        if nums[0] < nums[-1]:
            return nums[0]
        else:
            return min(self.findMin(nums[:mid]),self.findMin(nums[mid:])) 
        