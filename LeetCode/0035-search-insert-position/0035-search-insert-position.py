class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        i, min_offset = float("inf"), float("inf")

        while l <= r:
            m = (l + r) // 2
            offset = abs(nums[m] - target)
            if target > nums[m]:
                l = m + 1
                if offset < min_offset:
                    min_offset = offset
                    i = m + 1
            elif target < nums[m]:
                r = m - 1
                if offset < min_offset:
                    min_offset = offset
                    i = m
            else:
                return m
        return i
