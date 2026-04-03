class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapl = dict()
        for i in nums:
            mapl[i] = mapl.get(i, 0) + 1
        keys_only = sorted(mapl, key=lambda x: mapl[x],reverse=True)
        return keys_only[:k]