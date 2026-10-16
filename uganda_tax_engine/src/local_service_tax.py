from decimal import Decimal
from src.tax_base import Tax


class LocalServiceTax(Tax):
    """
    Simple configurable Local Service Tax.
    """

    def __init__(self, rate="0.01"):
        self.rate = Decimal(rate)

    def calculate(self, ctx):
        return ctx.total_income * self.rate