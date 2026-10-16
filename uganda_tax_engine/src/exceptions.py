class TaxError(Exception):
    """Base tax exception."""
    pass


class ValidationError(TaxError):
    """Invalid input data."""
    pass


class NoScheduleForDateError(TaxError):
    """No tax schedule exists for date."""
    pass