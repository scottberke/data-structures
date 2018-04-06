# O(n + n + n) => O(3n) => O(n) We go through the message once to reverse it,
# a second time to get each words start and end index and then a third time to
# reverse each word back to original word
# O(w) space where w is number of words in message due to storing the start and
# end indices of each word in an array. This could be reduced to O(1) if they
# were reversed after each start/end pair is found.
def reverse_message(message):
    """
    Input:
        ([chars]) = Array of chars that represents a message. The chars spell a
                    however the words are in reverse order.
    Output:
        (string) = String thats the message reversed
    """
    # Reverse characters in the entire message
    reverse(message, 0, len(message) - 1)
    # Figure out where each reversed word starts and ends
    word_start_end_indices = find_word_start_end_indices(message)
    # Reverse characters in each word back to normal
    for pair in word_start_end_indices:
        start, end = pair
        reverse(message, start, end)

    return ''.join(message)

def reverse(arr, start_index, end_index):
    """
    Input:
        ([chars]) = Array of chars that represents a message
        (int) = Index to start the reverse from
        (int) = Index to start the end reverse from
    Output:
        ([chars]) = Array of reversed chars from start index to end index
    """
    while start_index < end_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index += 1
        end_index -= 1

def find_word_start_end_indices(arr):
    """
    Input:
        ([chars]) = Array of chars that represents a message
    Output:
        ([(int, int)]) = Array of tuples representing start and end indices
                        for each word in the input
    """
    word_start_ends = []
    start_index = 0
    end_index = 0
    while end_index < (len(arr) - 1):
        end_index = find_word_end(start_index, arr)
        pair = (start_index, end_index)
        word_start_ends.append(pair)
        end_index += 2
        start_index = end_index

    return word_start_ends

def find_word_end(start_index, arr):
    """
    Input:
        (int) = Index of where to start searching for the next space/word end
        ([chars]) = Array of chars that represents a message
    Output:
        (int) = Index of the words end character
    """
    length = len(arr)
    while arr[start_index].isalpha():
        start_index += 1
        if start_index >= length:
            return start_index - 1

    return start_index - 1
