# This approach utilizes a Max Heap to poll k elements
# We should be able to build our heap in O(n * log n) where n is number of values and
# we should be able to poll k elements in O(k).
# Total runtime should be (k + n * log n) where n is size of input array and k
# is number of elements to be returned

def k_largest(arr, k):
    """
    Input:
        [int] = Array of ints to find the k largest items
        int = Number of elements to be returned
    Output:
        [int] = Array of k largest values
    """
    # Create heap
    heap = MaxHeap()
    # Build heap
    for i in arr:
        heap.add(i)

    # Poll max heap k times and return k_largest
    k_largest = []
    for _ in range(k):
        largest = heap.poll()
        if largest:
            k_largest.append(largest)

    return k_largest

class MaxHeap(list):
    def __init__(self):
        pass

    def add(self, val):
        """
        Input:
            int = Value to be added to heap
        Output:
            True if success
        """
        self.append(val)
        val_index = len(self) - 1
        self.bubble_up(val_index)

    def bubble_up(self, index):
        """
        Input:
            int = Index to start bubbling up from
        Output:
            True if success
        """
        parent_index = (index - 1) // 2
        if index > 0 and self[index] > self[parent_index]:
            self[index], self[parent_index] = self[parent_index], self[index]
            return self.bubble_up(parent_index)
        else:
            return True

    def poll(self):
        """
        Output:
            int = Max value in the heap
        """
        if len(self):
            self[0], self[-1] = self[-1], self[0]
            max = self.pop()
            self.bubble_down(0)
            return max
        else:
            return False

    def bubble_down(self, index):
        """
        Input:
            int = Index to start bubbling down from
        Output:
            True if success
        """
        child_index_a = (index * 2) + 1
        child_index_b = (index * 2) + 2

        if child_index_a < len(self) and child_index_b < len(self):
            swap_index = child_index_a if self[child_index_a] >= self[child_index_b] else child_index_b
        elif child_index_a < len(self):
            swap_index = child_index_a
        else:
            swap_index = None

        if swap_index and self[swap_index] > self[index]:
            self[index], self[swap_index] = self[swap_index], self[index]
            return self.bubble_down(swap_index)
        else:
            return True
