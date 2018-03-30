# O(n) where n is the length of the string
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
    # Accumulator for result integer
    res = 0
    # Enumerate index and 10s place from indices
    for index, value in enumerate(string[::-1]):
        # Raise and error if we dont have an integer or negative sign
        if not value.isdigit() and not value == '-':
            raise AttributeError("Invalid Input: {}".format(value))
        elif value == "-":
            # Convert to negative if we have negative sign
            res *= -1
        else:
            # Value = 10^(10s place) * (unicode value of string -  unicode value of 0)
            res += 10**index * (ord(value) - ord('0'))

    return res
