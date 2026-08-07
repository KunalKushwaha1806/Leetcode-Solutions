class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        if grid[0][0]==1:
            return 0
        if grid[r-1][c-1]:
            return 0
        @cache
        def S(i,j):
            if i==r-1 and j==c-1:
                return 1
            if i>=r or j>=c or grid[i][j]==1:
                return 0

            down=S(i+1,j)

            right=S(i,j+1)
            
            return down + right
        
        return S(0,0)
        