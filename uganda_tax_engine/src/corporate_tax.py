from decimal import Decimal
from src.tax_base import Tax


class CorporateTax(Tax):

    def calculate(
        self,
        revenue,
        expenses
    ):

        revenue = Decimal(str(revenue))
        expenses = Decimal(str(expenses))

        taxable_income = (
            revenue - expenses
        )

        return taxable_income * Decimal("0.30")