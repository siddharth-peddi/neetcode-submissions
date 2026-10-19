from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        queue = deque([(0,0,1)])
        grid[0][0] = 1

        directions = [(0,1),(-1,0),(1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        while queue:
            row, col, distance = queue.popleft()
            if row == n-1 and col == n-1:
                return distance
                            
            for dr, dc in directions:
                new_r = row + dr
                new_c = col + dc
                                
                if new_r < 0 or new_c < 0 or new_r >= n or new_c >= n:
                    continue
                if grid[new_r][new_c] == 0:
                    grid[new_r][new_c] = 1
                    queue.append((new_r, new_c, distance + 1))
        return -1 