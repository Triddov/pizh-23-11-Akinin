class Rectangle:
    def __init__(self, width, height):
        self.__w = self.__validate(width)
        self.__h = self.__validate(height)

    def __validate(value):
        return abs(value)

    def set_width(self, width):
        self.__w = self.__validate(width)

    def set_height(self, height):
        self.__h = self.__validate(height)

    def get_width(self):
        return self.__w

    def get_height(self):
        return self.__h

    def __str__(self):
        return f"Rectangle {self.__w}x{self.__h}"

a = Rectangle(3, 4)
print(a.get_width())
a.set_width(5)
print(a)
