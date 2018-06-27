import pdb
class Node():
    def __init__(self, name="", children=None):
        self.name = name
        if not children:
            self.children = []
        else:
            self.children = children

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None  # None


def create_dir_struct(dir_struct, root=None):
    if not root:
        root = Node()
    tree_root = root

    for dir in dir_struct:
        if type(dir) == list:
            root = create_dir_struct(dir, root)
        else:
            root = add_dir(root, dir)
    return tree_root

def add_dir(root, dir):
    child = root.find_child(dir)
    if not child:
        new_child = Node(dir)
        root.children.append(new_child)
        return new_child
    elif child.name != dir:
        add_dir(child, dir)
    else:
        return child


input = [   ["opt", "etc", "config"],
            ["usr"],
            ["usr", "include"],
            ["usr", "local"],
            ["usr", "local", "bin"],
            ["usr", "local", "include"],
            ["usr", "shared", "man", "gpg" ] ]


"""
Input:
Output:
"""


def myAtoi(string):
    res = 0
    for i in range(len(string)):
        res = res*10 + (ord(string[i]) - ord('0'))
    return res


def increment(y):
    if y == 0:
        return 1
    else:
        if y%2 == 1:
            return (2*increment(y//2))
        else:
            return (y + 1)
def to_b(num):
    res = ''
    while num > 0:
        if num % 2 == 1:
            res = '1' + res
            num -= 1
            num = num // 2
        else:
            res = '0' + res
            num = num / 2
    return res

def to_b(num):
    res = ''
    while num > 0:
        if num % 2 == 1:
            res += '1'
            num -= 1
        else:
            res  '0'
            num = num / 2
    return res


piece = [0, 1, 2]
board = [   [0, 1, 2],
            [1, 2, 0],
            [0, 1, 2]]
def convert_board_to_int(board):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            val = piece[board[i][j]]
            sum = sum * 3 + val
    return sum


for i in range(3):
    for j in range(3):
        for k in range(3):
            print(i, j, k)


def sort_based_on(string1, string2):
    look_up = {}
    for s_i in range(len(string2)):
        char = string2[s_i]
        look_up[char] = s_i

    counts = {}
    for s_i in range(len(string1)):
        char = string1[s_i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    res = ''
    for char in string2:
        count = counts[char]
        res += (char * count)

    for char in string1:
        if char not in string2:
            res += char

    return res
from avl_tree import *
avl = AVLTree()
avl.insert(6)
avl.insert(3)
avl.insert(15)
prettyPrint(avl.root)
               0    1     2    3   4    5    6    7    8    9   10    11   12  13   14   15
  message = [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]
            [ 's', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 'c', 'a', 'k', 'e', ]


def reverse(message):
    start_index = 0
    end_index = len(message) - 1
    while start_index < end_index:
        message[start_index], message[end_index] = message[end_index], message[start_index]
        start_index += 1
        end_index -= 1

    word_start_index = 0
    word_end_index = 0
    word_start_ends = []
    while word_end_index != end_index:
          word_end_index = find_word_end(start_index, message)
          pair = (start_index, word_end_index)
          word_start_ends.append(pair)
          word_start_index = word_end_index + 1
          word_end_index += 1

    for pair in word_start_ends:
        start_index, end_index = pair
        while start_index < end_index:
            message[start_index], message[end_index] = message[end_index], message[start_index]
            start_index += 1
            end_index -= 1

def find_word_end(start_index, arr):
    length = len(arr)
    while arr[start_index].isalpha():
        start_index += 1
        if start_index >= length:
            return start_index - 1

    return start_index - 1
