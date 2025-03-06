import math


class Vector3D:
    """
       A class to represent a three-dimensional vector

       Attributes:
           _x (float): X coordinate
           _y (float): Y coordinate
           _z (float): Z coordinate

       Methods:
           display(): Prints the vector coordinates
           read(): Reads vector coordinates from user input
           __add__(other): Performs vector addition
           __sub__(other): Performs vector subtraction
           __mul__(other): Computes the dot product or scalar multiplication
           __matmul__(other): Computes the cross product
           __call__(): Calculates the magnitude of the vector
           __repr__(): Returns a string representation of the object
    """

    def __init__(self, x=0, y=0, z=0):
        """
            Initializes a Vector3D object.

            Args:
                x (float, int): X coordinate (default is 0).
                y (float, int): Y coordinate (default is 0).
                z (float, int): Z coordinate (default is 0).
        """
        self._x = x
        self._y = y
        self._z = z

    def display(self):
        """ Prints the vector coordinates """
        print(f"Vector is ({self._x}, {self._y}, {self._z})")

    def read(self):
        """ Reads vector coordinates from user input  """
        self._x, self._y, self._z = map(float, input("Enter x, y, z: ").split())

    def __add__(self, other):
        """ Operator + : Performs vector addition """
        if isinstance(other, Vector3D):
            return Vector3D(self._x + other._x, self._y + other._y, self._z + other._z)
        raise TypeError("Operand must be of type Vector3D")

    def __sub__(self, other):
        """ Operator - : Performs vector subtraction """
        if isinstance(other, Vector3D):
            return Vector3D(self._x - other._x, self._y - other._y, self._z - other._z)
        raise TypeError("Operand must be of type Vector3D")

    def __mul__(self, other):
        """
           Operator * : Performs either dot product or scalar multiplication.

           Args:
               other (Vector3D or number): Another vector or a scalar.

           Returns:
               float or Vector3D: Dot product result or a new scaled vector.
       """
        if isinstance(other, Vector3D):
            return self._x * other._x + self._y * other._y + self._z * other._z
        elif isinstance(other, (int, float)):
            return Vector3D(self._x * other, self._y * other, self._z * other)
        raise TypeError("Operand must be a number or Vector3D")

    def __matmul__(self, other):
        """
          Operator @ : Performs cross product of two vectors.

          Args:
              other (Vector3D): Another vector.

          Returns:
              Vector3D: Resulting vector from the cross product.
      """
        if isinstance(other, Vector3D):
            return Vector3D(
                self._y * other._z - self._z * other._y,
                self._z * other._x - self._x * other._z,
                self._x * other._y - self._y * other._x
            )
        raise TypeError("Operand must be of type Vector3D")

    def __call__(self):
        """
         Computes the magnitude (length) of the vector when the object is called as a function

         Returns:
             float: Magnitude of the vector
     """
        return math.sqrt(self._x ** 2 + self._y ** 2 + self._z ** 2)

    def __repr__(self):
        """ Returns a string representation of the objec """
        return f"Vector3D({self._x}, {self._y}, {self._z})"



v1 = Vector3D(4, 1, 2)
v1.display()

v2 = Vector3D()
v2.read()

v3 = Vector3D(1, 2, 3)
v4 = v1 + v2
v4.display()

a = v4 * v3
print("Скалярное произведение (dot product):", a)

v5 = v1 @ v3
v5.display()
print("length v1:", v1())
