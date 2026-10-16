from decimal import Decimal


class TaxContext:
    """
    Holds payroll information needed by tax modules.
    """

    def __init__(
        self,
        gross_pay,
        allowances=0,
        resident=True
    ):
        self.gross_pay = Decimal(str(gross_pay))
        self.allowances = Decimal(str(allowances))
        self.resident = resident

    @property
    def total_income(self):
        return self.gross_pay + self.allowances