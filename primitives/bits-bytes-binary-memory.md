## Binary, Bits, Bytes and Memory
### Binary
#### Description:
The number system that we commonly use is base 10. We have digits 0-9 and when we reach 9 we roll over or carry the a one to the tens place. `10` represents 1 ‘ten’ and zero ‘ones’.  Computers only understand ones and zeros thus the number system understood by computers is base two using 0 and 1. When you reach 1 and want to increment the count to represent 2, you roll over or carry a one to the ‘twos place’. `10`  in binary represents 2 -> you have 1 ‘two’ and zero ‘ones’.
```
Base 10:
10^0 => 1
10^1 => 10
10^2 => 100
10^3 => 1000
etc

123 == 1 * 10^2 + 2 * 10^1 + 3 * 10^0

Base 2:
2^0 => 1
2^1 => 2
2^2 => 4
2^3 => 8
2^4 => 16
2^5 => 32
etc

11110 == 1 * 2^4 + 1 * 2^3 + 1 * 2^2 + 1 * 2^1 + 1 * 2^0 == 30
```
- One binary digit == one bit

### Bits and Bytes
Inside of a computer exists really only transistors. These have the ability to be switched on or off. Switched off, or the absence of electricity, represents a 0 while switched on, or presence of electricity, represents a 1. This provides the ability to count in binary.

8 bits represent one byte. In order for computers to represent numbers and letters, bits are grouped into bytes and encodings are used to translate between bytes and letters or numbers.
For example: `01000001 == 65 == ‘A’`  as the number 65 represents the letter ‘A’ in ASCII. Common encoding schemes are ASCII, Unicode and UTF.
- Fractions can be stored by storing two numbers -> denominator and numerator
- Decimals can be stored by just keeping track of where the decimal point goes
- Negative numbers can be stored by reserving the left most bit for the sign -> 0 == positive, 1 == negative
- Bits and Bytes are stored in memory

### Memory
When a computer needs to keep track of information it uses working memory or RAM. Think of RAM has having ‘shelves’. Each shelf holds 8 bits or 1 byte. Each shelf has a number or address identifying its location within memory. A memory controller is directly connected to each RAM shelf and is what does the reading and writing of information.
- - - -
