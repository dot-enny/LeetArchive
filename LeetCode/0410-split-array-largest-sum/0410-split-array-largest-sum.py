class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)
        res = high
        while low <= high:
            mid = (low + high) // 2
            sub_arrays = 0
            prefix_sum = 0
            for n in nums:
                if prefix_sum + n <= mid: prefix_sum += n
                else: 
                    prefix_sum = n
                    sub_arrays += 1
            sub_arrays += 1
            if sub_arrays <= k: 
                res = min(res, mid)
                high = mid - 1
            else: low = mid + 1
        return res

            