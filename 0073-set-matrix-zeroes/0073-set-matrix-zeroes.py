class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        fc = False
        fr = False

        for i in range(n):
            if matrix[i][0] == 0:
                fc = True
                break

        for j in range(m):
            if matrix[0][j] == 0:
                fr = True
                break

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if fr:
            for j in range(m):
                matrix[0][j] = 0

        if fc:
            for i in range(n):
                matrix[i][0] = 0