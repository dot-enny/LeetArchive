class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_first: bool) -> int:
            l, r = 0, len(nums) - 1
            idx = -1

            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    idx = m
                    if is_first:
                        r = m - 1  # keep searching left
                    else:
                        l = m + 1  # keep searching right
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return idx

        return [find_bound(True), find_bound(False)]