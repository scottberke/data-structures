def atoi(string):
    """
    Input:
        string (str) = String that can be converted to an integer.
                       Can be positive or negative number
    Output:
        (int)  = Integer value of the string

    Ex:
        atoi("1234") => 1234
    """
    # Grab string indices that correspond to 10s place of integer
    indices = list(reversed(range(len(string))))
    # Accumulator for result integer
    res = 0
    # Enumerate index and 10s place from indices
    for place, index in enumerate(indices):
        # Raise and error if we dont have an integer or negative sign
        if not string[index].isdigit() and not string[index] == '-':
            raise AttributeError("Invalid Input: {}".format(string[index]))
        elif string[index] == "-":
            # Convert to negative if we have negative sign
            res *= -1
        else:
            # Value = 10^(10s place) * (unicode value of string -  unicode value of 0)
            res += 10**place * (ord(string[index]) - ord('0'))
            
    return res
