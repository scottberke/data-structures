# Arrays
## Description:
In general, an array is a container for other values.  As a collection of values, arrays store these values at indices in a contiguous block of memory. Python refers to arrays as lists. When you create an array and store it in a variable name, the variable refers to the memory location of the contiguous block of memory allocated to the array.

Elements in an array are accessed by their index. For example if we had an array `arr` then we could access the nth element of this array via `arr[n]`. Arrays allow for constant time **O(1)** lookup of elements.

The address of an elements is calculated by taking the `nth address = start address + (n * size of each item)` . This formula works when arrays when the size of each element is the same and the array is stored in a contiguous block of memory.

This process changes when you have dynamic arrays. In languages like C, you need to allocate memory for an array prior to building the array where as languages like Ruby or Python allow you to use an array while managing the memory under the hood in a dynamic fashion. Most languages provide support for iterating over an array.

Multi-dimensional arrays, or arrays of arrays, can be used to represent graphs and matrices.

A **string is an array of characters**.

## Practice Problems
- [Check Permutations](../practice_problems/misc/practice_problems.md#check-permutations)

## Common Operations:
### Python

```python
# Create
>>> arr = []
>>> arr
[]

# Insertion - O(1)
>>> arr.append('tacos')  
>>> arr.append('tequila')
>>> arr.append('whiskey')
>>> arr
['tacos', 'tequila', 'whiskey']

>>> arr.insert(1, 'salsa')  	# O(n)
>>> arr
['tacos', 'salsa', 'tequila', 'whiskey']

# Concatenation - O(k) where k == size of concatenated list
>>> foods = ['tacos', 'salsa'] + ['burrito', 'cheese']
>>> foods
['tacos', 'salsa', 'burrito', 'cheese']

# Access - O(1)
>>> arr[0]
'tacos'
>>> arr[1]
'tequila'
>>> arr[-1]
'whiskey'

>>> arr.index('tacos') # o(n)
0

# Slice - O(k) where k is size of slice
>>> arr[:-1]
['tacos', 'tequila']
>>> arr[1:]
['tequila', 'whiskey']
>>> arr[:1]
['tacos']

# Modify - O(1)
>>> arr[1] = 'Lime'
>>> arr
['tacos', 'Lime', 'tequila', 'whiskey']


# Remove - O(1)
>>> arr.remove('Lime')  # O(n)
>>> arr
['tacos', 'tequila', 'whiskey']

>>> arr.pop()   # O(n) if index supplied due to shifting the remaining
'whiskey'
>>> arr
['tacos', 'tequila']

# Length - O(1)
>>> len(arr)
2

# Sort - O(n log n)
>>> foods.sort()
>>> foods
['burrito', 'cheese', 'salsa', 'tacos']

# Iteration - O(n)
>>> for element in arr:
...     print(element)
...
tacos
Lime
tequila
whiskey

# Copy - O(n)
>>> mex = arr[::]
>>> mex
['tacos', 'Lime', 'tequila', 'whiskey']
>>> arr
['tacos', 'Lime', 'tequila', 'whiskey']
>>> mex[0] = 'burrito'
>>> mex
['burrito', 'Lime', 'tequila', 'whiskey']
>>> arr
['tacos', 'Lime', 'tequila', 'whiskey']

# Clear O(1)
>>> arr.clear()
>>> arr
[]
```

### Ruby
[Docs](http://ruby-doc.org/core-2.4.1/Array.html)
```ruby
# Create
[1] pry(main)> arr = []
=> []
[2] pry(main)> arr = Array.new
=> []
[3] pry(main)> arr = Array.new(4)
=> [nil, nil, nil, nil]
[4] pry(main)> arr = Array.new(4, 'tacos')
=> ["tacos", "tacos", "tacos", "tacos"]

# Accessing - O(1)
[5] pry(main)> arr = ['tacos', 'tequila', 'whiskey']
=> ["tacos", "tequila", "whiskey"]
[6] pry(main)> arr[0]
=> "tacos"
[7] pry(main)> arr[-1]
=> "whiskey"
[8] pry(main)> arr.first
=> "tacos"
[9] pry(main)> arr.last
=> "whiskey"

# Inserting - O(1)
[11] pry(main)> arr.push('salsa', 'cheese')
=> ["tacos", "tequila", "whiskey", "salsa", "cheese"]
[12] pry(main)> arr.insert(1, 'jalapenos')	# O(n) due to reordering
=> ["tacos", "jalapenos", "tequila", "whiskey", "salsa", "cheese"]

# Slicing - O(k) where k is size of slice
[14] pry(main)> arr.take(3)
=> ["tacos", "jalapenos", "tequila"]
[16] pry(main)> arr[1..3]
=> ["jalapenos", "tequila", "whiskey"]

# Size - O(1)
[19] pry(main)> arr.count
=> 6
[20] pry(main)> arr.length
=> 6

# Removing - O(1)
[21] pry(main)> arr.pop
=> "cheese"
[22] pry(main)> arr
=> ["tacos", "jalapenos", "tequila", "whiskey", "salsa"]
[23] pry(main)> arr.pop(2)
=> ["whiskey", "salsa"]
[24] pry(main)> arr.pop(2)
=> ["jalapenos", "tequila"]
[25] pry(main)> arr
=> ["tacos"]

[27] pry(main)> arr.delete_at(2) # O(n) due to reordering
=> "tequila"
[28] pry(main)> arr
=> ["tacos", "jalapenos", "whiskey", "salsa"]
```
