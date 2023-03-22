def file_input(input_file, output_file, explain):
    """
    This function takes a string and returns the contents of the file as a string
    ----------
    Parameters
    ----------
    input: str
        A string representing the input from the command line
    ----------
    Returns
    ----------
    file_contents: str
        A string representing the contents of the file
    """
    # open the file
    # read the file
    # return the file contents
    with open(input_file, "r", encoding='utf-8-sig') as file:
        file_contents = file.read()
    # Convert the file to a list of lists of integers, where each list is a row in the csv
    file_contents = file_contents.split("\n")
    # remove the last element in the list, as it is an empty string
    file_contents = file_contents[:-1]
    file_contents = [i.split(",") for i in file_contents]
    # Check all the values in the list are integers
    for i in file_contents:
        for j in i:
            if j.isnumeric() == False:
                print("Input file must only contain integers")
                return False
    # convert the list of lists to a list of lists of integers
    for i in range(len(file_contents)):
        for j in range(len(file_contents[i])):
            file_contents[i][j] = int(file_contents[i][j])
    
    return file_contents

print(file_input("input.csv"))