# Task1 - Roman Numerals Class 

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


# Task2 - Pizzeria Terminal System

## Task Description

4.3.2.  Пиццерия предлагает клиентам Три вида пиццы: Пепперони, Барбекю и Дары Моря, каждая из которых 
определяется тестом, соусом и начинкой.
Требуется спроектировать и реализовать приложение для терминала, позволяющее обеспечить обслуживание посетителей.
Дополнительная информация
В бизнес-процессе работы пиццерии в контексте задачи можно выделить
3 сущности (объекта):
• Терминал: отвечает за взаимодействие с пользователем:
• вывод меню на экран;
• прием команд от пользователя (выбор пиццы, подтверждение заказа, оплата и др.);
Заказ: содержит список заказанных пицц, умеет подсчитывать свою стоимость;

Пицца: содержит заявленные характеристики пиццы, а также умеет себя подготовить (замесить тесто, собрать ингредиенты и т.д.), испечь, порезать и упаковать.
Т.к. пиццерия реализует несколько видов пиццы, которые различаются характеристиками, логично будет сделать общий класс Пицца, а в дочерних классах (например, классе ПиццаБарбекю) уточнить Характеристики
конкретной пиццы.


## Class Descriptions

### `Pizza`

**Description:** Represents a base pizza with attributes such as name, dough type, sauce, toppings, and price.

**Methods:**

- `__init__(self, name, dough, sauce, toppings, price)`: Initializes a pizza with specified attributes.
- `__str__(self)`: Returns a string representation of the pizza.
- `prepare(self)`: Simulates pizza preparation.
- `bake(self)`: Simulates baking the pizza.
- `cut(self)`: Simulates cutting the pizza.
- `pack(self)`: Simulates packing the pizza.

### `PepperoniPizza`

**Description:** A subclass of `Pizza` representing a pepperoni pizza.

**Methods:**

- `__init__(self)`: Initializes a pepperoni pizza with predefined attributes.

### `BBQPizza`

**Description:** A subclass of `Pizza` representing a BBQ pizza.

**Methods:**

- `__init__(self)`: Initializes a BBQ pizza with predefined attributes.

### `SeafoodPizza`

**Description:** A subclass of `Pizza` representing a seafood pizza.

**Methods:**

- `__init__(self)`: Initializes a seafood pizza with predefined attributes.

### `Order`

**Description:** Represents a customer order containing multiple pizzas.

**Methods:**

- `__init__(self)`: Initializes an empty order with a unique order number.
- `__str__(self)`: Returns a string representation of the order.
- `add_pizza(self, pizza)`: Adds a pizza to the order.
- `total(self)`: Calculates and returns the total price of the order.
- `process(self)`: Processes the order by preparing, baking, cutting, and packing pizzas.

### `Terminal`

**Description:** Manages customer interactions, allowing them to place an order and complete payment.

**Methods:**

- `__init__(self)`: Initializes the terminal with a predefined menu.
- `show_menu(self)`: Displays available pizzas.
- `handle_command(self, choice)`: Handles a customer’s pizza selection.
- `accept_payment(self)`: Simulates payment processing.
- `run(self)`: Runs the terminal, allowing interactive order placement.

