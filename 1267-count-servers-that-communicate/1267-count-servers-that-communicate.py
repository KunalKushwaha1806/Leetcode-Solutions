class Solution(object):
    def countServers(self, grid):
        m, n = len(grid), len(grid[0])
        row_cnt = [0] * m
        col_cnt = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_cnt[i] > 1 or col_cnt[j] > 1:
                        cnt += 1
        return cnt    