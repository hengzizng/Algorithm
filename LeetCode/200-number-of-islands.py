from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            stack = deque([(x, y)])            
            while stack:
                x, y = stack.pop()
                if 0 <= x < len(grid) and \
                   0 <= y < len(grid[0]) and \
                   grid[x][y] == '1':
                    grid[x][y] = '0'
                    stack.append((x-1, y))
                    stack.append((x+1, y))
                    stack.append((x, y-1))
                    stack.append((x, y+1))
        
        number_of_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(row, col)
                    number_of_islands += 1
                    
        return number_of_islands
