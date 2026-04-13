class Solution:
    def cutter(self, array, l, r):
        # Base case: single element
        if r - l == 1:
            return array[l]

        # If this segment is not rotated, min is at the left
        if array[l] <= array[r - 1]:
            return array[l]

        m = (r + l) // 2
        return min(self.cutter(array, l, m), self.cutter(array, m, r))

    def findMin(self, nums: List[int]) -> int:
        return self.cutter(nums, 0, len(nums))