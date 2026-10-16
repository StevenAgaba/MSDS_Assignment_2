from decimal import Decimal
from src.tax_base import Tax


class NSSF(Tax):

    def calculate(self, ctx):

        employee = (
            ctx.total_income
            * Decimal("0.05")
        )

        employer = (
            ctx.total_income
            * Decimal("0.10")
        )

        return {
            "employee": employee,
            "employer": employer
        }
