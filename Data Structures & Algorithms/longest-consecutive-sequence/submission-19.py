class Solution:

    def find(self, x, array):
        if x == array[x]:
            return x
        array[x] = self.find(array[x], array)  # path compression
        return array[x]

    def union(self, array, x, y):
        array[self.find(y, array)] = self.find(x, array)

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        parent = list(range(len(nums)))
        num_to_index = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if num + 1 in num_to_index:
                self.union(array=parent, x=i, y=num_to_index[num + 1])
        print(parent)
        print(num_to_index)
        from collections import Counter
        group_sizes = Counter(self.find(i, parent) for i in range(len(nums)))
        print(group_sizes)
        return max(group_sizes.values())
 