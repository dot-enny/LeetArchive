class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        find = { n:i for i, n in enumerate(nums1) }
        stack = []
        
        for i in range(len(nums2)):
            while stack and (nums2[i] > stack[-1]):
                find_idx = find[stack[-1]]
                res[find_idx] = nums2[i]
                stack.pop()
            if nums2[i] in find:
                stack.append(nums2[i])

        return res