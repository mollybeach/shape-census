from shape_census import count_connected_shapes
from file_reader import read_grid_from_file

def process_file(filename):
    """
    Process a file containing a grid and count the connected shapes.

    Args:
    filename (str): The name of the file to process.

    Returns:
    int: The number of connected shapes in the grid, or None if an error occurred.
    """
    grid = read_grid_from_file(filename)
    if grid is not None:
        shape_count = count_connected_shapes(grid)
        print(f"Processed {filename}: Found {shape_count} shapes")
        return shape_count
    return None

def main():
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

if __name__ == "__main__":
    main()
