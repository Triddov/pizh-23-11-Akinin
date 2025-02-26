import re
import unittest


class Roman:
    """
    A class representing Roman numerals, supporting arithmetic operations and conversions.
    """
    ROMAN_NUMERAL_MAP = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }

    def __init__(self, value):
        """
        Initializes a Roman numeral object.
        :param value: An integer or a valid Roman numeral string.
        """
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("Roman numerals must be positive")
            self.value = value
            self.roman = self.int_to_roman(value)
        elif isinstance(value, str):
            if not re.fullmatch(r'^[MDCLXVI]+$', value):
                raise ValueError("Invalid Roman numeral")
            self.roman = value
            self.value = self.roman_to_int(value)
        else:
            raise TypeError("Unsupported data type")

    @staticmethod
    def roman_to_int(roman):
        """
        Converts a Roman numeral string to an integer.
        :param roman: A string representing a Roman numeral.
        :return: The integer value of the Roman numeral.
        """
        result, prev_value = 0, 0
        for char in reversed(roman):
            value = Roman.ROMAN_NUMERAL_MAP[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result

    @staticmethod
    def int_to_roman(number):
        """
        Converts an integer to a Roman numeral string.
        :param number: An integer to be converted.
        :return: A string representing the Roman numeral.
        """
        result = ""
        for roman, value in Roman.ROMAN_NUMERAL_MAP.items():
            while number >= value:
                result += roman
                number -= value
        return result

    def __add__(self, other):
        return Roman(self.value + other.value)

    def __sub__(self, other):
        if self.value - other.value <= 0:
            raise ValueError("Result cannot be zero or negative in Roman numerals")
        return Roman(self.value - other.value)

    def __mul__(self, other):
        return Roman(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        result = self.value // other.value
        if result < 1:
            raise ValueError("Result of division is too small for Roman numerals")
        return Roman(result)

    def __str__(self):
        return self.roman

    def __repr__(self):
        return f"Roman('{self.roman}')"



a = Roman('X')   # 10
b = Roman(5)     # 'V'

print(a + b)     # 'XV' (10 + 5)
print(a - b)     # 'V' (10 - 5)
print(a * b)     # 'L' (10 * 5)
print(a / b)     # 'II' (10 / 5)
