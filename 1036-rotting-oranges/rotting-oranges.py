from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Step 1: count fresh oranges & push rotten ones to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:  # rotten orange
                    q.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:  # fresh orange
                    fresh += 1

        # Step 2: BFS to rot neighbors
        time = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c, t = q.popleft()
            time = max(time, t)  # track latest time
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # make it rotten
                    fresh -= 1
                    q.append((nr, nc, t + 1))

        # Step 3: if fresh left, return -1
        return -1 if fresh > 0 else time
