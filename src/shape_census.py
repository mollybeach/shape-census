def count_connected_shapes(grid):
    """
    Count the number of connected shapes in a binary grid.

    A shape is defined as a group of adjacent '1's connected horizontally or vertically.
    Diagonal connections are not considered.

    Args:
    grid (List[str]): A 2D grid represented as a list of strings, where each string is a row
                      of '0's and '1's.

    Returns:
    int: The number of distinct connected shapes in the grid.

    Example:
    >>> grid = ['110', '010', '011']
    >>> count_connected_shapes(grid)
    2
    """
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
