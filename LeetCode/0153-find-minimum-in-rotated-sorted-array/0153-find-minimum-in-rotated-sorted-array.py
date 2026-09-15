class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]: return nums[0]

        l, r, min = 0, len(nums) - 1, nums[-1]
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= min:
                min = nums[m]
                r = m - 1
            else: l = m + 1
        
        return min