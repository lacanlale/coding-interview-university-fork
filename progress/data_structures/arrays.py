class Vector():
    def __init__(self):
        self.vals = []

    def size(self) -> int:
        """
        number of items
        """
        return len(self.vals)
    
    def capacity(self) -> int:
        """
        number of items it can hold
        """
        pass

    def is_empty(self) -> bool:
        pass

    def insert(self, num: int, ind: int):
        """
        inserts item at index, shifts that index's value and trailing elements to the right
        """
        pass

    def push(self, num: int):
        pass

    def at(self, ind: int) -> int:
        """
        returns the item at a given index, blows up if index out of bounds
        """
        return self.vals[ind]

    def prepend(self, num: int):
        self.insert(num, 0)

    def pop(self):
        """
        remove from end, return value
        """
        pass

    def delete(self, num: int):
        """
        delete item at index, shifting all trailing elements left
        """
        pass

    def remove(self, num: int):
        """
        looks for value and removes index holding it (even if in multiple places)
        """
        pass

    def find(self, item: int) -> int:
        """
        looks for value and returns first index with that value, -1 if not found
        """
        return -1

    def resize(self, num: int):
        """
        when you reach capacity, resize to double the size
        when popping an item, if the size is 1/4 of capacity, resize to half
        """
        pass
