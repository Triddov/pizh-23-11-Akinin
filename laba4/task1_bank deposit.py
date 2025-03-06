from abc import ABC, abstractmethod


class Deposit(ABC):
    """Abstract class representing a bank deposit."""

    def __init__(self, amount: float, term: int, rate: float):
        """Initializes the deposit with amount, term (years), and annual interest rate."""
        self.amount = amount  # Initial deposit amount
        self.term = term  # Deposit term in years
        self.rate = rate  # Annual interest rate

    @abstractmethod
    def calculate_profit(self) -> float:
        """Method to calculate the profit from the deposit."""
        pass

    def total_amount(self) -> float:
        """Total amount at the end of the deposit term."""
        return self.amount + self.calculate_profit()


class FixedDeposit(Deposit):
    """Fixed-term deposit (simple interest)."""

    def calculate_profit(self) -> float:
        return self.amount * self.rate * self.term / 100


class BonusDeposit(Deposit):
    """Bonus deposit (bonus is added if amount exceeds a threshold)."""
    BONUS_THRESHOLD = 100000  # Minimum amount for bonus eligibility
    BONUS_PERCENT = 5  # Bonus percentage on profit

    def calculate_profit(self) -> float:
        profit = self.amount * self.rate * self.term / 100

        if self.amount > self.BONUS_THRESHOLD:
            profit += profit * self.BONUS_PERCENT / 100
        return profit


class CapitalizedDeposit(Deposit):
    """Compound interest deposit."""

    def calculate_profit(self) -> float:
        return self.amount * ((1 + self.rate / 100) ** self.term - 1)


def select_deposit():
    """Function to allow user to select a deposit type."""
    print("Select deposit type:")
    print("1 - Fixed-term deposit")
    print("2 - Bonus deposit")
    print("3 - Compound interest deposit")

    choice = int(input("Enter the option number: "))
    amount = float(input("Enter deposit amount: "))
    term = int(input("Enter deposit term (years): "))
    rate = float(input("Enter annual interest rate: "))

    if choice == 1:
        deposit = FixedDeposit(amount, term, rate)
    elif choice == 2:
        deposit = BonusDeposit(amount, term, rate)
    elif choice == 3:
        deposit = CapitalizedDeposit(amount, term, rate)
    else:
        print("Invalid choice!")
        return

    print(f"Profit from deposit: {deposit.calculate_profit():.2f}")
    print(f"Total amount at the end of term: {deposit.total_amount():.2f}")


if __name__ == "__main__":
    select_deposit()

# Example usage:
# deposit1 = FixedDeposit(50000, 3, 5)
# print(deposit1.calculate_profit())  # Output: Profit calculation
# print(deposit1.total_amount())  # Output: Total amount at end of term

# deposit2 = BonusDeposit(120000, 2, 4)
# print(deposit2.calculate_profit())  # Output: Profit with bonus
# print(deposit2.total_amount())  # Output: Total amount at end of term
