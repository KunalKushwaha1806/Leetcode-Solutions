class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD=10**9 + 7 
        r=len(grid)
        c=len(grid[0])
        memo={}
        def dfs(i,j,d):
            if i<0 or i>=r or j<0 or j>=c:
                return 0
            if i == r-1 and j == c-1:
                return 1
            pair=(i,j,d)
            if pair in memo:
                return memo[pair]
            if grid[i][j]==1:
                if d==0:
                    return dfs(i+1,j,1)
                else:
                    return dfs(i,j+1,0)

            memo[(i,j,d)]=dfs(i+1,j,1)+dfs(i,j+1,0)% MOD
            return memo[(i,j,d)]
        return (dfs(0,1,0)+dfs(1,0,1))% MOD


        