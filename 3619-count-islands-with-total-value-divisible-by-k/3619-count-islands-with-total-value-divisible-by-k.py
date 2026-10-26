class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        r=len(grid)
        c=len(grid[0])
        ans=0
        def dfs(i,j):
            if i<0 or i>=r or j<0 or j>=c or grid[i][j]==0:
                return 0
            value=grid[i][j]
            grid[i][j]=0

            value+=dfs(i-1,j)
            value+=dfs(i+1,j)
            value+=dfs(i,j-1)
            value+=dfs(i,j+1)

            return value
        for i in range(r):
            for j in range(c):
                if grid[i][j]>0:
                    if dfs(i,j)%k==0:
                        ans+=1
        return ans