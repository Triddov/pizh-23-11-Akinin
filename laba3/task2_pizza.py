class Pizza:
    """
    Base class representing a pizza with its attributes and methods.
    """

    def __init__(self, name, dough, sauce, toppings, price):
        """
        Initializes a pizza with name, dough type, sauce, toppings, and price.
        """
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the pizza.
        """
        return f"{self.name} with {self.dough} dough, {self.sauce} sauce, toppings: {', '.join(self.toppings)}. Price: ${self.price}"

    def prepare(self):
        """
        Simulates the preparation of the pizza.
        """
        print(f"Preparing {self.name}...\n")

    def bake(self):
        """
        Simulates baking the pizza.
        """
        print(f"Baking {self.name}...\n")

    def cut(self):
        """
        Simulates cutting the pizza.
        """
        print(f"Cutting {self.name}...\n")

    def pack(self):
        """
        Simulates packing the pizza.
        """
        print(f"Packing {self.name}...\n")


class PepperoniPizza(Pizza):
    """
    Class representing a Pepperoni pizza.
    """

    def __init__(self):
        """
        Initializes a Pepperoni Pizza with specific attributes.
        """
        super().__init__("Pepperoni Pizza", "Thin crust", "Tomato", ["Pepperoni", "Cheese"], 10.99)


class BBQPizza(Pizza):
    """
    Class representing a BBQ pizza.
    """

    def __init__(self):
        """
        Initializes a BBQ Pizza with specific attributes.
        """
        super().__init__("BBQ Pizza", "Thick crust", "BBQ", ["Chicken", "Onions", "Cheese"], 12.99)


class SeafoodPizza(Pizza):
    """
    Class representing a Seafood pizza.
    """

    def __init__(self):
        """
        Initializes a Seafood Pizza with specific attributes.
        """
        super().__init__("Seafood Pizza", "Regular crust", "White sauce", ["Shrimp", "Mussels", "Cheese"], 14.99)


class Order:
    """
    Class representing a customer's order, containing multiple pizzas.
    """
    order_counter = 0

    def __init__(self):
        """
        Initializes an empty order and assigns a unique order number.
        """
        self.ordered_pizzas = []
        Order.order_counter += 1
        self.order_number = Order.order_counter

    def __str__(self):
        """
        Returns a string representation of the order.
        """
        return f"\nOrder {self.order_number}: {len(self.ordered_pizzas)} pizza(s), Total: ${self.total()}"

    def add_pizza(self, pizza):
        """
        Adds a pizza to the order.
        """
        self.ordered_pizzas.append(pizza)

    def total(self):
        """
        Calculates and returns the total price of the order.
        """
        return sum(pizza.price for pizza in self.ordered_pizzas)

    def process(self):
        """
        Processes the order by preparing, baking, cutting, and packing all pizzas.
        """
        print(f"Processing {self}...")
        for pizza in self.ordered_pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.pack()


class Terminal:
    """
    Class representing the terminal for interacting with customers.
    """

    def __init__(self):
        """
        Initializes the terminal with a predefined menu and an empty order.
        """
        self.menu = [PepperoniPizza(), BBQPizza(), SeafoodPizza()]
        self.order = None

    def show_menu(self):
        """
        Displays the available pizzas in the menu.
        """
        print("Menu:")
        for i, pizza in enumerate(self.menu, start=1):
            print(f"{i}. {pizza}")

    def handle_command(self, choice):
        """
        Handles the customer's choice and adds the corresponding pizza to the order.
        """
        if choice in range(1, len(self.menu) + 1):
            self.order.add_pizza(self.menu[choice - 1])
            print(f"Added {self.menu[choice - 1].name} to order.")

    def accept_payment(self):
        """
        Simulates payment processing.
        """
        print(f"Payment of ${self.order.total()} received. Thank you!")

    def run(self):
        """
        Runs the terminal, allowing customers to place an order interactively.
        """
        self.order = Order()
        self.show_menu()
        while True:
            choice = input("\nEnter pizza number to add to order (or 'done' to finish): ")
            if choice.lower() == "done":
                break
            if choice.isdigit() and 1 <= int(choice) <= len(self.menu):
                self.handle_command(int(choice))
            else:
                print("Invalid choice. Please try again.")
        print(self.order)
        self.accept_payment()
        self.order.process()


if __name__ == "__main__":

    terminal = Terminal()
    terminal.run()


    # order = Order()
    # order.add_pizza(PepperoniPizza())
    # order.add_pizza(BBQPizza())
    # print("ЗАказ: ", order)
    # order.process()
