def count_connected_shapes(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    shape_count = 0

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0' or visited[i][j]:
            return
        visited[i][j] = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in directions:
            dfs(i + di, j + dj)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and not visited[i][j]:
                dfs(i, j)
                shape_count += 1

    return shape_count
