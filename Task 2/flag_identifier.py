# This script will read the input from the command line (flags and values) and pass them on to the appropriate function 
import sys
def input_checker(user_input):
    """
    This function performs a simple check, to see if the command line input consists of valid flags and values only
    ----------
    Parameters
    ----------
    input: str  
        A string representing the input from the command line
    ----------

    Returns
    ----------
    bool
        A boolean representing whether the input is valid or not


    """
    legal_flags = ["-explain", "-file", "-hint", "-profile"]
    # if -file is present remove the two values after it from the input
    if "-file" in user_input:
        user_input = user_input[:user_input.index("-file")] + user_input[user_input.index("-file")+3:] 
    # if -hint is present remove the value after it from the input
    if "-hint" in user_input:
        user_input = user_input[:user_input.index("-hint")] + user_input[user_input.index("-hint")+2:]
    # remove all the flags from the input
    for flag in legal_flags:
        if flag in user_input:
            user_input.remove(flag)
    # if there are any values left in the input, return False
    if len(user_input) > 0:
        print("Invalid flags inputted")
        return False
    else:
        return True

def read_flags(user_input):
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
        if flag in user_input:
            flag_dict[flag] = True

    # if file is in input, set flag value to a list of next two values (input and output)
    if "-file" in user_input:
        # Input and outputs should be the next two values after the flag respectively.
        input_file = user_input[user_input.index("-file")+1]
        output_file = user_input[user_input.index("-file")+2]

        # check if the input and output files are csv's
        for i in [input_file, output_file]:
            if i[-4:] != ".csv":
                print("Input and output files must be a csv's")
                return False
            
        # check if the input file exists
        try:
            open(input_file, "r")
        except FileNotFoundError:
            print("Grid input file not found")
            return False

        #If these conditions are met, set the flag value to the next two values (input and output)     
        flag_value["-file"] = user_input[user_input.index("-file")+1:user_input.index("-file")+3]

    # if hint is in input, set flag value to the integer after the flag
    if "-hint" in user_input:
        # check if the hint value is an integer
        try:
            int(user_input[user_input.index("-hint")+1])
        except ValueError:
            print("Hint value must be an integer")
            return False
        else:
            flag_value["-hint"] = int(user_input[user_input.index("-hint")+1])
    
    return flag_dict, flag_value




if __name__ == "__main__":
    print(input_checker(sys.argv[1:]))
    read_flags(sys.argv[1:])
