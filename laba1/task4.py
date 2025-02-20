class Rectangle:
    def __init__(self, width, height, sign):
        self.w = width
        self.h = height
        self.s = sign

    def __str__(self):
        return '\n'.join([self.s * self.w] * self.h)

    def __add__(self, other):
        return Rectangle(self.w + other.w, self.h + other.h, self.s)

a = Rectangle(4, 2, 'w')
b = Rectangle(8, 3, 'z')

print(a)
print(b)
print(a + b)
