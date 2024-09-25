import os

def read_grid_from_file(filename):
    """
    Read a grid from a file.

    Args:
    filename (str): The name of the file to read.

    Returns:
    list of str: The grid as a list of strings, or None if an error occurred.
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, '..', 'data', filename)
        print(f"Attempting to open file: {file_path}")
        
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading {filename}: {str(e)}")
        return None
