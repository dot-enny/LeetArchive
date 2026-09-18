class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            left = float('-inf') if (m - 1) < 0 else nums[m - 1]
            mid = nums[m]
            right =  float('-inf') if (m + 1) > (n - 1) else nums[m + 1]
            if left < mid and mid > right: return m
            elif mid < right: l = m + 1
            elif mid < left: r = m - 1


        
            