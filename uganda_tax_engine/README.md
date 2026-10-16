# Uganda Tax Engine

## Agaba Steven. 
### Registration Number: S26M19/002. 
### Access Number: B38624

## Overview

The Uganda Tax Engine is a Python Object-Oriented Programming (OOP) project that computes taxes and statutory deductions based on Uganda Revenue Authority (URA) tax rules.

The project demonstrates the use of:

- Abstract Classes
- Inheritance
- Encapsulation
- Exception Handling
- Decimal Arithmetic
- Operator Overloading
- Unit Testing
- Modular Software Design

## Implemented Modules

### PAYE (Pay As You Earn)

Calculates PAYE using Uganda tax bands.

### NSSF

Calculates:

- Employee Contribution (5%)
- Employer Contribution (10%)

### Local Service Tax (LST)

Implements a configurable Local Service Tax deduction.

### Corporate Income Tax

Calculates corporate tax based on taxable income.

### Tax Planner

Compares different tax scenarios and reports tax differences.

## Project Structure

```text
uganda_tax_engine/
│
├── src/
│   ├── exceptions.py
│   ├── money.py
│   ├── tax_base.py
│   ├── tax_context.py
│   ├── paye.py
│   ├── nssf.py
│   ├── local_service_tax.py
│   ├── corporate_tax.py
│   ├── payroll.py
│   └── planner.py
│
├── tests/
│   └── test_taxes.py
│
├── Uganda_Tax_Engine.ipynb
├── README.md
└── requirements.txt
```

## Features

- Uganda PAYE calculations
- NSSF contributions
- Local Service Tax deductions
- Corporate tax calculations
- Payroll processing
- Tax scenario analysis
- Boundary value testing
- OOP-based implementation

## How to Run

1. Install required packages:

```bash
pip install -r requirements.txt
```

2. Open Jupyter Notebook:

```bash
jupyter notebook
```

3. Open:

```text
Uganda_Tax_Engine.ipynb
```

4. Run all cells from top to bottom.

## Why Decimal Was Used

Tax calculations require exact arithmetic.

Using floating-point numbers can introduce rounding errors:

```python
0.1 + 0.2
```

Result:

```python
0.30000000000000004
```

To avoid inaccuracies, the project uses Python's Decimal class for all monetary calculations.

## OOP Design

The project uses an abstract base class:

```python
Tax
```

The following classes inherit from it:

- PAYE
- NSSF
- LocalServiceTax
- CorporateTax

Each class implements its own:

```python
calculate()
```

method.

## Testing

Boundary-value tests were performed using:

- 335000
- 335001
- 410000
- 485000
- 10000000
- 10000001

to verify tax-band correctness.

## AI Assistance Declaration

Microsoft Copilot was used to:

- Understand assignment requirements
- Explain Python OOP concepts
- Debug implementation issues
- Review project structure

All code was reviewed, tested, and understood by the author before submission.

## Author

Steven Agaba