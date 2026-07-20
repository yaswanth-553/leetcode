class Solution(object):
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        lst = []
        for i in range(m):
            for j in range(n):
                lst.append(grid[i][j])
        k %= (m * n)
        lst = lst[-k:]+lst[:-k]
        ans = []
        index = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(lst[index])
                index += 1
            ans.append(row)
        return ans