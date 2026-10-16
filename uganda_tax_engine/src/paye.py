from decimal import Decimal
from src.tax_base import Tax


class PAYE(Tax):

    def calculate(self, ctx):

        income = ctx.total_income

        if income <= Decimal("335000"):
            tax = Decimal("0")

        elif income <= Decimal("410000"):
            tax = (
                Decimal("15000")
                + (income - Decimal("335000"))
                * Decimal("0.25")
            )

        elif income <= Decimal("485000"):
            tax = (
                Decimal("33750")
                + (income - Decimal("410000"))
                * Decimal("0.30")
            )

        elif income <= Decimal("10000000"):
            tax = (
                Decimal("56250")
                + (income - Decimal("485000"))
                * Decimal("0.30")
            )

        else:
            tax = (
                Decimal("2910750")
                + (income - Decimal("10000000"))
                * Decimal("0.40")
            )

        if not ctx.resident:
            tax *= Decimal("1.10")

        return tax