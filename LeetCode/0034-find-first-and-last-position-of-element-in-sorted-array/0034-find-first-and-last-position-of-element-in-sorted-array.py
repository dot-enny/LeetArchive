class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        res = [-1, -1]
        if not n: return res
        m = 0
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]: r = m - 1
            elif target > nums[m]: l = m + 1
            else: 
                res[0], res[1] = m, m
                break
        target_idx = m

        l, r = 0, target_idx - 1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]: l = m + 1
            elif target == nums[m]:
                res[0] = m
                r = m - 1

        l, r = target_idx + 1, n - 1
        while l <= r: 
            m = (l + r) // 2
            if target < nums[m]: r = m - 1
            elif target == nums[m]:
                res[1] = m
                l = m + 1

        return res