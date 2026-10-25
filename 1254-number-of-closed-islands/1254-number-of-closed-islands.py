class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        def dfs(i, j):
            if i<0 or i>=r or j<0 or j>=c:
                return False
            if grid[i][j]==1:
                return True
            grid[i][j]=1
            up=dfs(i-1,j)
            down=dfs(i+1,j)
            left=dfs(i,j-1)
            right=dfs(i,j+1)
            return up and down and left and right
        ans=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    if dfs(i,j):
                        ans+=1
        return ans

