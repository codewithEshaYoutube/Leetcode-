class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # if we’ve matched the full word
            if i == len(word):
                return True
            # boundary checks + mismatch check
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                board[r][c] != word[i]):
                return False

            # mark visited
            temp, board[r][c] = board[r][c], "#"
            # explore neighbors
            found = (dfs(r+1, c, i+1) or 
                     dfs(r-1, c, i+1) or 
                     dfs(r, c+1, i+1) or 
                     dfs(r, c-1, i+1))
            # backtrack
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

