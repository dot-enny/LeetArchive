class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        find = defaultdict()
        for i in range(len(nums1)): 
            find[nums1[i]] = i    

        for i in range(len(nums2)):
            if nums2[i] in find:
                for j in range(i+1, len(nums2)):
                    if nums2[j] > nums2[i]:
                        res[find[nums2[i]]] = nums2[j]
                        break
        return res
                
