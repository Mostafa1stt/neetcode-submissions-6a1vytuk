class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1,len(nums)):
                if -(nums[i]+nums[j]) in seen:
                    sortedo = [nums[i], nums[j], -(nums[i]+nums[j])]
                    sortedo.sort()
                    if sortedo in output:
                        continue
                    output.append(sortedo)
                seen.add(nums[j])
        return output