class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if m == len(nums) - 1: return nums[m]
            if m == 0: return nums[m]
            if nums[m - 1] != nums[m] and nums[m + 1] != nums[m]: return nums[m]
            if m % 2 == 0:
                if nums[m - 1] == nums[m]: r = m - 1
                elif nums[m + 1] == nums[m]: l = m + 1
            else:
                if nums[m - 1] == nums[m]: l = m + 1
                elif nums[m + 1] == nums[m]: r = m - 1