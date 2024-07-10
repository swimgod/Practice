from typing import List, Optional


class NumOfIslands:
    @staticmethod
    def numIslands(grid: List[List[str]]) -> int:
        # Track visited nodes
        # Return early for base case on recursive function
        # Check surrounding nodes for continuation of adjacent land nodes
        visited = set()
        num_rows = len(grid)
        num_cols = len(grid[0])
        island_count = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= num_rows or col >= num_cols or ((row, col) in visited):
                return
            visited.add((row, col))
            print(f"Current Point: ({row}, {col})")
            print(f"Down: ({row+1}, {col})")
            print(f"Up: ({row-1}, {col})")
            print(f"Right: ({row}, {col+1})")
            print(f"Left: ({row}, {col-1})")
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1" and ((r, c) not in visited):
                    dfs(r, c)
                    island_count += 1
        return island_count
