import random


class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        # Get the index of the element to be removed
        index = self.val_to_index[val]

        # Swap the element with the last element
        last_val = self.values[-1]
        self.values[index] = last_val
        self.val_to_index[last_val] = index

        # Remove the last element
        self.values.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
