# O(n) where n is the length of one of the strings
def one_away(string, string_perm):
    # If the diff is > 1 then we know its more than one away
    if abs(len(string) - len(string_perm)) > 1:
        return False
    # Track our diffs found and each strings index
    diffs = 0
    string_i = 0
    perm_i = 0
    # We really only need to check as long as one string still has chars
    while perm_i < len(string_perm):
        try:
            # Check if the chars at the index are different
            if string[string_i] != string_perm[perm_i]:
                # Increment diffs if they are
                diffs += 1
                # If the strings are diff lens, we need to hold back an index
                if len(string) < len(string_perm):
                    string_i -= 1
                elif len(string) > len(string_perm):
                    perm_i -= 1
        # If we've reached an index error on a string we've found a diff
        except IndexError:
            diffs += 1
        # Cut short if we've reached > 1 diff
        if diffs > 1:
            return False
        # Increment our indices
        string_i += 1
        perm_i += 1

    # If we've reached here without cutting short theres < 2 diffs     
    return True
