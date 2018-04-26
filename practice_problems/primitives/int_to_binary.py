# O(log n) where n is the number. n is halved each iteration
def int_to_binary(int):
    res = ''
    while int > 0:
        res = str(int % 2) + res
        int = int // 2
    return res
