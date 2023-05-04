# Further Computer Programming - Group 32 - Sudoku Solver

This repo comprises a set of code used to solve sudoku puzzles. There are multiple implementations of the solver. The options are:
- running main file without flags to solve a pre loaded set of grids
- running main file with INPUT to solve that grid
- running the class directly using class implementation

For all these see ** USAGE **

## Structure
The project is structured in the following way:

The main file is `main.py`. This file contains the main run of the sudoku solver for running either preloaded grids or an INPUT flag grid file.

The main file uses the `sudoku.py` which stores the class for the solver. Each class method calls the various methods defined in the module functions:
- `explain.py`
- `file_input.py`
- `flag_identifier.py`
- `hint.py`
- `modules.py`
- `possible_values.py`
- `profile_docs.py`


The `requirements.txt` file contains the required packages to run the program.


#### Flags

All flags can be used together in any combination and order

The FLAGS are optional and can be used to change the behaviour of the program. The following flags are available:

`-explain`
- the program will explain the steps it takes to solve the sudoku or provide a list of applied hints if requested.
`-hint [N]`
- N argument is the requested number of hints. This must be an integer. The program will provide N hints to the user along with a partially solved grid.
`-profile`
- the program will profile the time it takes to solve the sudoku using available methods and compare the results via a graph.
`-file [INPUT] [OUTPUT]` 
- both files must be .csv, can be used to specify the input and output file. The input file must be a csv in the working directory. The output file will be created in the working directory. 


The `Sudoku.py` file contains the Sudoku class. This class contains the methods to solve the sudoku.
The solver options are:
- `recursion_solve()`
- `wavefront_solve()`
- `overall_solve()` - uses a combination of quick solve and recursion solve


## Setup
To run the program, you need to have Python 3 installed. 

To install the required packages, run the following command in the terminal:
```
pip install -r requirements.txt
```

## Usage


1. To run the program on a pre loaded set of grids, run the following command in the terminal:
```
python main.py FLAGS
```
You may need to specify the python version:

```
python3 main.py FLAGS
```

2. To run the program on an input file with a grid, run the following command in the terminal: 

```
python main.py -file INPUT.csv OUTPUT.csv FLAGS

```

3. To run the class directly, open a script and follow the example in the Sudoku class. 



#### NOTE - profile

The standard `time.time()` function provides sub-second precision, though that precision varies by platform. For Linux and Mac precision is +- 1 microsecond or 0.001 milliseconds. Python on Windows uses +- 16 milliseconds precision due to clock implementation problems due to process interrupts. 

As a result we have now used `time.perf_counter()` for all profilling uses.





