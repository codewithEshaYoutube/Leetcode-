from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        # Flatten board into 1D (index = cell number)
        cells = [-1] * (n * n + 1)
        num, left_to_right = 1, True
        for r in range(n - 1, -1, -1):
            cols = range(n) if left_to_right else range(n - 1, -1, -1)
            for c in cols:
                cells[num] = board[r][c]
                num += 1
            left_to_right = not left_to_right

        # BFS
        q = deque([(1, 0)])      # (cell, moves)
        visited = {1}

        while q:
            pos, steps = q.popleft()
            if pos == n * n:     # reached last cell
                return steps
            for dice in range(1, 7):
                nxt = pos + dice
                if nxt <= n * n:
                    # If ladder/snake exists, move there
                    dest = cells[nxt] if cells[nxt] != -1 else nxt
                    if dest not in visited:
                        visited.add(dest)
                        q.append((dest, steps + 1))
        return -1
