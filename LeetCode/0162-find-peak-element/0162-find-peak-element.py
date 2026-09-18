class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            if (m > 0) and nums[m - 1] > nums[m]: r = m - 1
            elif (m < (n - 1)) and nums[m + 1] > nums[m]: l = m + 1
            else: return m


        
            