# O(n) over all time complexity 
def check_permutations(first_str, second_str):
    look_up = {}
    # O(1)
    if len(first_str) != len(second_str):
        return False
    # O(n)
    for char in first_str:
        if char in look_up:
            look_up[char] += 1
        else:
            look_up[char] = 1
    # O(n)
    for char in second_str:
        if char not in look_up:
            return False
        else:
            look_up[char] -= 1
            if look_up[char] < 0:
                return False
    # O(1)
    if sum(look_up.values()) == 0:
        return True
    else:
        return False
