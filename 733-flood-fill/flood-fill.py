from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 1. Get the original color of the starting pixel
        start_color = image[sr][sc]

        # 2. If the starting pixel already has the target color → nothing to do
        if start_color == color:
            return image

        # 3. Get the number of rows and columns
        rows, cols = len(image), len(image[0])

        # 4. DFS function to color a pixel and spread to its neighbors
        def dfs(r, c):
            # a) Stop if (r,c) is out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # b) Stop if this pixel is not the original start color
            if image[r][c] != start_color:
                return

            # c) Change this pixel to the new color
            image[r][c] = color

            # d) Spread to 4 neighbors
            dfs(r+1, c)  # Down
            dfs(r-1, c)  # Up
            dfs(r, c+1)  # Right
            dfs(r, c-1)  # Left

        # 5. Start DFS from the given starting pixel
        dfs(sr, sc)

        # 6. Return the updated image
        return image
