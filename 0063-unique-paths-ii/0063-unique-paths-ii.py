class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        if grid[0][0]==1:
            return 0
        if grid[r-1][c-1]:
            return 0
        memo=[[-1]*(c+1) for _ in range(r+1)]
        def S(i,j):
            
            if i==r-1 and j==c-1:
                return 1
            if i>=r or j>=c or grid[i][j]==1:
                return 0
            if memo[i][j]!=-1:
                return memo[i][j]

            down=S(i+1,j)

            right=S(i,j+1)
            
            memo[i][j]=down + right
            return memo[i][j]
        
        return S(0,0)
        