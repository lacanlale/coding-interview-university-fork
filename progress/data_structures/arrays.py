from math import inf
class Vector():
    def __init__(self, length):
        if length <= 16:
            self.vector = [-inf] * 16
        elif length > 16 and length <= 32:
            self.vector = [-inf] * 32
        elif length > 32 and length <= 64:
            self.vector = [-inf] * 64
        else:
            self.vector = [-inf] * 128
        self.length = 0

    def size(self) -> int:
        """
        number of items
        """
        return self.length
    
    def capacity(self) -> int:
        """
        number of items it can hold
        """
        return len(self.vector)

    def is_empty(self) -> bool:
        return self.vector[0] == -inf

    def insert(self, num: int, ind: int):
        """
        inserts item at index, shifts that index's value and trailing elements to the right
        """
        curr_size = self.size()
        if curr_size == self.capacity() or curr_size + 1 == self.capacity():
            self.resize(curr_size * 2)

        right = self.vector[ind:-1]
        self.vector[ind] = num

        for i, val in enumerate(right):
            self.vector[ind+1+i] = val
        self.length += 1

    def push(self, num: int):
        """
        adds at the end
        """
        self.insert(num, self.size())

    def at(self, ind: int):
        """
        returns the item at a given index, blows up if index out of bounds
        """
        if ind < self.size():
            return self.vector[ind]
        else:
            raise IndexError

    def prepend(self, num: int):
        self.insert(num, 0)

    def pop(self):
        """
        remove from end, return value
        """
        val = self.vector[self.size()-1]
        self.vector[self.size()] = -inf
        self.length -= 1
        return val

    def delete(self, ind: int):
        """
        delete item at index, shifting all trailing elements left
        """
        if ind < self.size():
            right = self.vector[ind+1:] + [-inf]

            for i, val in enumerate(right):
                self.vector[i+ind] = val

            self.length -= 1

            if self.size()/self.capacity() <= 0.25:
                self.resize(int(self.capacity()/2))

    def remove(self, num: int):
        """
        looks for value and removes index holding it (even if in multiple places)
        """
        i = 0
        while i < self.size():
            if self.vector[i] == num:
                self.delete(i)
                continue
            i += 1
        
    def find(self, item: int) -> int:
        """
        looks for value and returns first index with that value, -1 if not found
        """
        for ind, val in enumerate(self.vector):
            if val == -inf:
                break
            if val == item:
                return ind
        return -1

    def resize(self, num: int):
        """
        when you reach capacity, resize to double the size
        when popping an item, if the size is 1/4 of capacity, resize to half
        """
        if num > self.capacity():
            self.vector += [-inf] * self.capacity()
        else:
            self.vector = self.vector[:num]

test = Vector(2)
print(f"Vector size: {test.size()}")
print(f"Vector capacity: {test.capacity()}")
if test.is_empty():
    print("Vector is empty")

print("\nTesting prepend and push...")
test.prepend(0)
test.push(1)
print(f"Vector size after adding items: {test.size()}")
for i in range(test.size()):
    print(f"Value at vector index {i}: {test.at(i)}")

try:
    print("\nAttempting to grab an item out of the current size.")
    print("\tThis should error")
    test.at(3)
except IndexError:
    print("IndexError exception caught")

print("\nTesting filling the vector up to its limit...")
for i in range(2, 16):
    test.push(i)
print(f"Vector size: {test.size()}")
print(f"Vector capacity: {test.capacity()}")

print("\nTesting insert and at functions with value 9999...")
test.insert(9999, 10)
print(f"Number 9999 found at index {test.find(9999)}")
print(f"Number at index 10: {test.at(10)}")
print(f"Number that does not exist in the array, -999: {test.find(-999)}")

print("\nTesting delete, remove, and pop...")
print(f"Checking for 9999, output: {test.find(9999)}")
print(f"Adding duplicate 9999 values to test removal")
for _ in range(5):
    test.push(9999)
print(f"Vector size after insert: {test.size()}")
test.remove(9999)
print(f"Vector size after removal: {test.size()}")
print(f"Checking for existing 9999: {test.find(9999)}")

print("\nTesting downsize...")
print(f"Vector size: {test.size()}")
print(f"Vector capacity: {test.capacity()}")
for i in range(8):
    test.delete(i)
print(f"Vector size after deleting: {test.size()}")
print(f"Vector capacity after deleting: {test.capacity()}")

