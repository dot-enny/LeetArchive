class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = []

        def dfs(curr_subset, i):
            if i == len(nums): 
                subsets.append(curr_subset)
                return

            s1 = curr_subset
            s2 = [*curr_subset, nums[i]]

            dfs(s1, i + 1)
            dfs(s2, i + 1)
        
        dfs([], 0)
        return subsets