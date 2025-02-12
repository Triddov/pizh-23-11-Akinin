from random import random

class RandomIterator:
    def __init__(self, quantity, minimum, maximum):
        self.qty = quantity
        self.low = minimum
        self.high = maximum

    def __iter__(self):
        return self

    def __next__(self):
        if self.qty == 0:
            raise StopIteration
        self.qty -= 1
        return random() * (self.high - self.low) + self.low
