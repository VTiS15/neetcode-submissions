class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        q = [(grid[0][0], 0, 0)]
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        
        while q:
            t, y, x = heapq.heappop(q)

            if y == x == n - 1:
                return t
            if (y, x) in visited:
                continue

            visited.add((y, x))
            for dy, dx in directions:
                new_y, new_x = y + dy, x + dx
                if new_y < 0 or new_x < 0 or new_y == n or new_x == n:
                    continue
                heapq.heappush(q, (max(t, grid[new_y][new_x]), new_y, new_x))
        

        