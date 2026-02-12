class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo={}
        
        def dfs(i, j):
            if i >= m or j >= n:
                return float('inf')
            
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if (i,j)in memo:
                return memo[(i,j)]
            
            right = dfs(i, j + 1)
            left = dfs(i + 1, j)
            
            memo[(i,j)]= grid[i][j] + min(right, left)
            return memo[(i,j)]
        
        return dfs(0, 0)
