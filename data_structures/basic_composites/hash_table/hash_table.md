# Hash Tables
## Description
A hash table, sometimes called an associative array, **maps keys and values**. The value add of a hash table is that **lookups are constant time O(1)** where as in an array or linked list you need to iterate through the data structure to find what you're looking for.

Hash tables work by taking a key and running it through a **hashing function**. The data associated with the key is then stored at the location obtained through the hashing of the key. When the key is used to subsequently look for the data, the key is again hashed in constant time to provide the location of the data.

The hashing function should create a unique output from the provided key but, that sometimes doesn't happen. When two keys create the same hashed output, this is known as a collision. When a **collision** occurs, data is stored in another data structure like a linked list or array.

Avoiding collisions by making use of a linked list is a common approach. Each spot in the hash tables array will map to a linked list of items. The linked list will contain the un-hashed key so that in the event of a collision, the hashed key is used to find the correct array bucket and the linked list is traversed to find the correct item. Collisions of this nature happen but are uncommon.

Linear probing is also a method for dealing with collisions. If a collision occurs, the hash table will look for an adjacent spot in the array to store the data. 

In Python, hash tables come in the form of a dict.
```python
>>> a = { 'tacos': 1 }
>>> type(a)
<class 'dict'>
>>> a['tacos']
1
```

## Implementation
- [Hash Table - Python](./hash_table.py)
- [Hash Table Test Cases - Python](./hash_table_test.py)
