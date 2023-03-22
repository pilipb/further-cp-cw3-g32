# This script will read the input from the command line (flags and values) and pass them on to the appropriate function 
import sys

def read_flag(input:str):
    """
    This function takes a string and returns the flag if it is a valid flag, otherwise it returns None
    ----------
    Parameters
    ----------
    input: str
        A string representing the input from the command line
    ----------
    Returns
    ----------
    flag: str
        A string representing the flag, or None
    """
    # create a list of valid flags
    # if there is an input not in the list of valid flags, return None

    flag_dict = {"-explain": False, "-file": False, "-hint": False, "-profile": False}
    flag_value = {"-file": None, "-hint": None}
    # if flag is in input, set flag dict value to True
    for flag in flag_dict:
        if flag in input:
            flag_dict[flag] = True
    # if file is in input, set flag value to a list of next two values
    if "-file" in input:
        flag_value["-file"] = input[input.index("-file")+1:input.index("-file")+3]
    # if hint is in input, set flag value to am integer of the next value
    if "-hint" in input:
        flag_value["-hint"] = int(input[input.index("-hint")+1])





    return flag_dict, flag_value
if __name__ == "__main__":
	print(read_flag(sys.argv[1:]))