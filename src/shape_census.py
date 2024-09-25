import os

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

def process_file(filename):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, '..', 'data', filename)
        print(f"Attempting to open file: {file_path}")
        
        with open(file_path, 'r') as file:
            grid = [line.strip() for line in file]
        
        shape_count = count_connected_shapes(grid)
        print(f"Processed {filename}: Found {shape_count} shapes")
        return shape_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while processing {filename}: {str(e)}")
        return None

if __name__ == "__main__":
    print("Script is running...")
    small_file = 'data_small.txt'
    large_file = 'data_large.txt'

    print(f"Processing {small_file}...")
    small_shapes = process_file(small_file)
    
    print(f"Processing {large_file}...")
    large_shapes = process_file(large_file)

    if small_shapes is not None:
        print(f"Number of connected shapes in {small_file}: {small_shapes}")
    if large_shapes is not None:
        print(f"Number of connected shapes in {large_file}: {large_shapes}")

    print("Script execution completed.")
