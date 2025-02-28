# Bank Deposits OOP

This project implements a banking deposit system using Object-Oriented Programming (OOP) principles in Python. The application allows users to select different types of deposits and calculate their expected profit.

## Features
- Supports three types of deposits:
  - **Fixed Deposit** (simple interest)
  - **Bonus Deposit** (bonus for high amounts)
  - **Capitalized Deposit** (compound interest)
- Uses an abstract base class (`Deposit`) to enforce structure.
- Includes a user input function for deposit selection.

## Classes and Methods

### `Deposit (Abstract Base Class)`
```python
class Deposit(ABC):
```
An abstract class representing a general bank deposit.

#### Methods:
- `__init__(self, amount: float, term: int, rate: float)`:
  Initializes the deposit with an amount, term (in years), and an annual interest rate.
- `calculate_profit(self) -> float` (abstract):
  Must be implemented by subclasses to compute profit.
- `total_amount(self) -> float`:
  Returns the total amount at the end of the deposit term (`initial amount + profit`).

### `FixedDeposit`
```python
class FixedDeposit(Deposit):
```
A simple fixed-term deposit that uses the formula for simple interest.

#### Methods:
- `calculate_profit(self) -> float`:
  Returns profit calculated as:
  ```
  profit = amount * rate * term / 100
  ```

### `BonusDeposit`
```python
class BonusDeposit(Deposit):
```
A deposit that provides a bonus if the initial amount exceeds a threshold.

#### Methods:
- `calculate_profit(self) -> float`:
  - Uses the simple interest formula.
  - If the deposit amount is greater than `BONUS_THRESHOLD` (100,000), an additional `BONUS_PERCENT` (5%) is added to the profit.

### `CapitalizedDeposit`
```python
class CapitalizedDeposit(Deposit):
```
A deposit where interest is compounded annually.

#### Methods:
- `calculate_profit(self) -> float`:
  Uses the compound interest formula:
  ```
  profit = amount * ((1 + rate / 100) ** term - 1)
  ```

### `select_deposit()`
```python
def select_deposit():
```
A function that prompts the user to select a deposit type and input values for amount, term, and interest rate.


## Usage Example
```python
deposit1 = FixedDeposit(50000, 3, 5)
print(deposit1.calculate_profit())  # Output: Profit calculation
print(deposit1.total_amount())      # Output: Total amount at end of term

# Bonus Deposit Example
deposit2 = BonusDeposit(120000, 2, 4)
print(deposit2.calculate_profit())  # Output: Profit with bonus
print(deposit2.total_amount())      # Output: Total amount at end of term
```

---

# Vector Class

## Description
The `Vector` class represents a 2D geometric vector and supports various operations such as addition, subtraction, scalar multiplication, normalization, and dot product. The class also provides methods to save and load vectors from JSON files and initialize vectors from a string representation.

## Installation
No additional libraries are required apart from the built-in `json` and `math` modules.

## Class Methods and Attributes

### Constructor
```python
Vector(x: float, y: float) -> None
```
Initializes a vector with given x and y coordinates.

### Special Methods
- `__str__() -> str`: Returns a string representation of the vector.
- `__add__(other: Vector) -> Vector`: Adds two vectors.
- `__sub__(other: Vector) -> Vector`: Subtracts two vectors.
- `__mul__(scalar: float) -> Vector`: Multiplies the vector by a scalar.
- `__truediv__(scalar: float) -> Vector`: Divides the vector by a scalar.

### Properties
- `x -> float`: Returns the x-coordinate of the vector.
- `y -> float`: Returns the y-coordinate of the vector.

### Class Methods
- `from_string(cls, str_value: str) -> Vector`: Creates a vector from a string representation, e.g., `Vector(3,4)`.
- `load(cls, filename: str) -> Vector`: Loads a vector from a JSON file.

### Instance Methods
- `save(filename: str) -> None`: Saves the vector to a JSON file.
- `magnitude() -> float`: Returns the magnitude of the vector.
- `normalize() -> Vector`: Returns a normalized unit vector.
- `dot_product(other: Vector) -> float`: Computes the dot product with another vector.

