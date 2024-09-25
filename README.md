# Shape Census

Shape Census is a Python-based tool designed to analyze grids of binary data and identify connected shapes within them. It's part of a programming challenge for Maestro AI, demonstrating skills in algorithm implementation, file handling, and problem-solving.

## Project Overview

In the world of Shape Census, we're dealing with a unique kind of population: shapes formed by connected '1's in a sea of '0's. Our census taker (the program) diligently scans through text files containing grids of 0's and 1's, identifying and counting distinct shapes along the way.

### Key Features

- Reads and processes grid data from text files
- Identifies shapes formed by adjacent '1's (considering up, down, left, right connections)
- Counts the total number of distinct shapes in each grid
- Handles varying grid sizes efficiently
- Provides clear output of results

## Project Structure

The project is organized as follows:

```
shape-census/
├── data/
│   ├── data_small.txt
│   ├── data_large.txt
├── src/
│   ├── __init__.py
│   ├── file_reader.py
│   ├── main.py
│   ├── shape_census.py
├── README.md
```

- `src/main.py`: The main entry point of the program, orchestrating the flow of execution.
- `src/shape_census.py`: Contains the core algorithm for counting connected shapes.
- `src/file_reader.py`: Handles reading grid data from files.
- `data/`: Directory containing the input data files.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/shape-census.git
   cd shape-census
   ```

2. Ensure you have Python 3.x installed on your system.

## Usage

To run the Shape Census program:


This will process both `data_small.txt` and `data_large.txt` files located in the `data/` directory and output the number of connected shapes found in each.

## How It Works

1. The program reads the grid data from the input files.
2. It uses a depth-first search (DFS) algorithm to identify connected shapes in the grid.
3. A shape is defined as a group of adjacent '1's connected horizontally or vertically (diagonal connections are not considered).
4. The program counts each distinct shape and provides a total count for each input file.

## Example Output

```
Processed data_small.txt: Found 2 shapes
Processed data_large.txt: Found 10 shapes
Number of connected shapes in data_small.txt: 2
Number of connected shapes in data_large.txt: 10
```


## Customization

To process different input files:
1. Place your new input files in the `data/` directory.
2. Modify the filenames in `src/main.py` to match your new input files.

## Contributing

Contributions to improve Shape Census are welcome. Please feel free to submit a Pull Request.

## License

[Specify your license here, e.g., MIT License, GPL, etc.]

## Contact

[Your Name] - [Your Email]

Project Link: [https://github.com/mollybeach/shape-census](https://github.com/yourusername/mollybeach)

---

Shape Census: Unveiling the hidden topography in your binary data landscapes!