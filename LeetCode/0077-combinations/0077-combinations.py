class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        
        def dfs(i, k, curr):
            if not k:
                res.append(curr.copy())
                return
            
            if i > n: return

            curr.append(i)
            dfs(i + 1, k - 1, curr)
            curr.pop()
            dfs(i + 1, k, curr)

        dfs(1, k, [])
        return res