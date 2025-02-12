from math import pi

class Cylinder:
    @staticmethod
    def make_area(d, h):
        return round(pi * d ** 2 / 4 * 2 + pi * d * h, 2)

    def __init__(self, diameter, height):
        self.__dict__['dia'] = diameter
        self.__dict__['h'] = height
        self.__dict__['area'] = self.make_area(diameter, height)

    def __setattr__(self, key, value):
        if key in {'dia', 'h'}:
            self.__dict__[key] = value
            self.__dict__['area'] = self.make_area(self.__dict__['dia'], self.__dict__['h'])
        elif key == 'area':
            print("Нельзя изменять площадь напрямую!")

a = Cylinder(1, 2)
print(a.dia, a.h, a.area)
