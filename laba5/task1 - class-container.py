import json
from typing import List, Any


class Vector:
    """
    A simple vector class with x and y coordinates.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def to_dict(self) -> dict:
        """Converts the vector to a dictionary format."""
        return {"x": self.x, "y": self.y}

    @classmethod
    def from_dict(cls, data: dict) -> 'Vector':
        """Creates a Vector instance from a dictionary."""
        return cls(data["x"], data["y"])


class VectorCollection:
    """
    A container class for storing and managing Vector objects.
    """

    def __init__(self) -> None:
        """Initializes an empty collection of vectors."""
        self._data: List[Vector] = []

    def __str__(self) -> str:
        """Returns a string representation of the vector collection."""
        return "[" + ", ".join(map(str, self._data)) + "]"

    def __getitem__(self, index: int) -> Vector:
        """Allows indexing and slicing of the vector collection."""
        return self._data[index]

    def add(self, value: Vector) -> None:
        """Adds a Vector to the collection."""
        self._data.append(value)

    def remove(self, index: int) -> None:
        """Removes a Vector from the collection by index."""
        if 0 <= index < len(self._data):
            del self._data[index]

    def save(self, filename: str) -> None:
        """Saves the vector collection to a JSON file."""
        with open(filename, "w") as file:
            json.dump([vector.to_dict() for vector in self._data], file, indent=4)

    def load(self, filename: str) -> None:
        """Loads the vector collection from a JSON file."""
        with open(filename, "r") as file:
            data = json.load(file)
            self._data = [Vector.from_dict(item) for item in data]


# Example usage
if __name__ == "__main__":
    collection = VectorCollection()
    collection.add(Vector(1, 2))
    collection.add(Vector(3, 4))
    print(collection)  # Output: [Vector(1, 2), Vector(3, 4)]
    collection.save("vectors.json")

    new_collection = VectorCollection()
    new_collection.load("vectors.json")
    print(new_collection)  # Output: [Vector(1, 2), Vector(3, 4)]
