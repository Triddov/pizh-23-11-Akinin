import json
from math import sqrt


class Vector:
    """
    A class representing a 2D geometric vector.

    Attributes:
        x (float): X-coordinate of the vector.
        y (float): Y-coordinate of the vector.
    """

    def __init__(self, x: float, y: float) -> None:
        """Initializes a Vector with x and y coordinates."""
        self._x: float = x
        self._y: float = y

    def __str__(self) -> str:
        """Returns a string representation of the vector."""
        return f"Vector({self._x}, {self._y})"

    def __add__(self, other: "Vector") -> "Vector":
        """Adds two vectors."""
        if isinstance(other, Vector):
            return Vector(self._x + other._x, self._y + other._y)
        raise TypeError("Operand must be a Vector")

    def __sub__(self, other: "Vector") -> "Vector":
        """Subtracts two vectors."""
        if isinstance(other, Vector):
            return Vector(self._x - other._x, self._y - other._y)
        raise TypeError("Operand must be a Vector")

    def __mul__(self, scalar: float) -> "Vector":
        """Multiplies the vector by a scalar."""
        if isinstance(scalar, (int, float)):
            return Vector(self._x * scalar, self._y * scalar)
        raise TypeError("Operand must be a number")

    def __truediv__(self, scalar: float) -> "Vector":
        """Divides the vector by a scalar."""
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector(self._x / scalar, self._y / scalar)
        raise ValueError("Cannot divide by zero")

    @property
    def x(self) -> float:
        """Returns the x-coordinate."""
        return self._x

    @property
    def y(self) -> float:
        """Returns the y-coordinate."""
        return self._y

    @classmethod
    def from_string(cls, str_value: str) -> "Vector":
        """Creates a Vector instance from a string."""
        try:
            x, y = map(float, str_value.strip("Vector() ").split(","))
            return cls(x, y)
        except ValueError:
            raise ValueError("Invalid string format")

    def save(self, filename: str) -> None:
        """Saves the vector to a JSON file."""
        with open(filename, "w") as f:
            json.dump({"x": self._x, "y": self._y}, f)

    @classmethod
    def load(cls, filename: str) -> "Vector":
        """Loads a vector from a JSON file."""
        with open(filename, "r") as f:
            data = json.load(f)
            return cls(data["x"], data["y"])

    def magnitude(self) -> float:
        """Returns the magnitude of the vector."""
        return sqrt(self._x ** 2 + self._y ** 2)

    def normalize(self) -> "Vector":
        """Returns a unit vector in the same direction."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return self / mag

    def dot_product(self, other: "Vector") -> float:
        """Computes the dot product with another vector."""
        if isinstance(other, Vector):
            return self._x * other._x + self._y * other._y
        raise TypeError("Operand must be a Vector")


#