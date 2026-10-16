from decimal import Decimal


class TaxPlanner:

    def compare(
        self,
        tax_a,
        tax_b
    ):

        difference = (
            Decimal(str(tax_a))
            - Decimal(str(tax_b))
        )

        return {
            "tax_a": tax_a,
            "tax_b": tax_b,
            "difference": difference
        }