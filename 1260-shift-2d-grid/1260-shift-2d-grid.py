class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        while k:
            ans = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m - 1 and j == n - 1:
                        ans[0][0] = grid[i][j]
                    elif j == n - 1:
                        ans[i + 1][0] = grid[i][j]
                    else:
                        ans[i][j + 1] = grid[i][j]
            grid = ans
            k -= 1
        return grid