class HashTable():
    def __init__(self, size=100):
        self.size = size
        self.buckets = [None] * self.size

    def __setitem__(self, key, val):
        key_hash = hash(key)
        bucket_loc = key_hash % self.size
        self.buckets[bucket_loc] = val

    def __getitem__(self, key):
        key_hash = hash(key)
        bucket_loc = key_hash % self.size
        return self.buckets[bucket_loc]


    # TODO Implement linked list in the buckets
    # to account for key collision and store key name

    # TODO Implement a call to display the hash table
