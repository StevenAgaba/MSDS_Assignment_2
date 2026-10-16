from decimal import Decimal


class Money:
    """
    Represents money in UGX using Decimal.
    """

    def __init__(self, amount):
        self.amount = Decimal(str(amount))

    def __add__(self, other):
        return Money(
            self.amount + other.amount
        )

    def __sub__(self, other):
        return Money(
            self.amount - other.amount
        )

    def __lt__(self, other):
        return self.amount < other.amount

    def __repr__(self):
        return f"UGX {self.amount:,.2f}"