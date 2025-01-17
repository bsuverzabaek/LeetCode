class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0

        def traverseIsland(grid, i, j):
            if grid[i][j] == '0':
                return

            grid[i][j] = '0'

            if i > 0:
                traverseIsland(grid, i - 1, j)

            if i < len(grid) - 1:
                traverseIsland(grid, i + 1, j)

            if j > 0:
                traverseIsland(grid, i, j - 1)

            if j < len(grid[0]) - 1:
                traverseIsland(grid, i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    traverseIsland(grid, i, j)
                    numOfIslands += 1

        return numOfIslands
