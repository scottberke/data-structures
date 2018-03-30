# O(n) where n is number of bits in binary number
def binary_to_int(binary):
    res = 0
    for index, bit in enumerate(list(binary)[::-1]):
        res += 2**index * int(bit)
    return res
