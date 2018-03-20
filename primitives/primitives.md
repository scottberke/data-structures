# Primitives

## Integers
Integers are typically represented by 4 bytes or 32 bits. Most of the time this memory allocation for an integer enables representation of negative and positive numbers.
`-2^31 -> 2^31 - 1` is the range of numbers represented by a 4 byte signed integer. If you have an unsigned integer then you effectively double the number of positive values capable of being represented to `2^32`
Other varieties of integers exists capable or storing larger number such as bigint.

- - - -

## Floating Point Numbers
Floating point numbers represent real numbers in computing. Computers suffer from floating point impression when doing calculations with floating point numbers.
Floating point numbers are typically represented as fixed number of significant digits and an exponent with a fixed base
Example: `3.4567 = 34567 * 10^-4`
Doubles store floating point numbers but double the precision. These usually take 8 bytes vs the 4 bytes usually reserved for a float.
- - - -

## Characters
Characters or chars are single characters and take up 1 byte. Character encoding allows 1 byte or 8 bits to be translated to a char. For example: `01000001 == 65 == ‘A’`  as the number 65 represents the letter ‘A’ in ASCII. Common encoding schemes are ASCII, Unicode and UTF.
- - - -

## Booleans
Booleans are the logical values of True and False.  Often times Booleans are represented as integers with 0 == False and 1 == True.  Booleans are typically returned by comparison operators such as > or < or ==.
- - - -

## Pointers
Pointers are values that point to another objects address in memory. These are sometimes called references. They enable access to specific locations in memory where larger or other types of data are stored. Dereferencing is when you access the underlying data at a pointers location. Pointers are used in linked lists and in variety of other data structures to reference other data.


## Practice Problems
- [atoi - String To Integer - Python](../practice_problems/primitives/atoi.py)
- [atoi - String To Integer Tests - Python](../practice_problems/primitives/atoi_test.py)
