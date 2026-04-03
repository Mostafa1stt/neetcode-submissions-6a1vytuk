class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapl = dict()
        for i , x in enumerate(nums):
            if (target - x ) in mapl:
                return  [mapl[target-x],i]
            mapl[x] = i
