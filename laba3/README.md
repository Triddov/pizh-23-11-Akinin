# Roman Numerals Class 

## Task Description

4.3.1. Римское число
Создайте класс Roman (РимскоеЧисло), представляющий римское число и поддерживающий операции +, -, *, /.

При реализации класса следуйте рекомендациям:
операции +, -, *, / реализуйте как специальные методы (__add__ и др.); методы преобразования имеет
смысл реализовать как статические методы, позволяя не создавать экземпляр объекта в случае,
если необходимо выполнить только преобразования чисел.

Implement a class `Roman` that represents a Roman numeral and supports arithmetic operations:
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)

The class should allow conversion between integers and Roman numerals.

## Class and Method Descriptions

### `Roman`
A class representing Roman numerals with arithmetic operations and conversion methods.

### `__init__(self, value)`
Initializes a Roman numeral object.
- **Parameters:** `value` (either an integer or a Roman numeral string)
- **Raises:**
  - `ValueError` if the integer is non-positive or the Roman numeral is invalid.
  - `TypeError` if the value is neither an integer nor a string.

### `roman_to_int(roman)` (Static Method)
Converts a Roman numeral string to an integer.
- **Parameters:** `roman` (string, a valid Roman numeral)
- **Returns:** Integer representation of the Roman numeral.

### `int_to_roman(number)` (Static Method)
Converts an integer to a Roman numeral string.
- **Parameters:** `number` (integer, positive)
- **Returns:** A string representing the Roman numeral.

### `__add__(self, other)`
Performs addition of two Roman numeral objects.
- **Returns:** A new `Roman` object representing the sum.

### `__sub__(self, other)`
Performs subtraction of two Roman numeral objects.
- **Returns:** A new `Roman` object representing the difference.
- **Raises:** `ValueError` if the result is zero or negative.

### `__mul__(self, other)`
Performs multiplication of two Roman numeral objects.
- **Returns:** A new `Roman` object representing the product.

### `__truediv__(self, other)`
Performs integer division of two Roman numeral objects.
- **Returns:** A new `Roman` object representing the quotient.
- **Raises:**
  - `ZeroDivisionError` if attempting to divide by zero.
  - `ValueError` if the result is less than 1 (too small for Roman numerals).

### `__str__(self)`
Returns the string representation of the Roman numeral.

### `__repr__(self)`
Returns a formal string representation of the object.


