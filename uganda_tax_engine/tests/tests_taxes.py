from src.paye import PAYE

paye = PAYE()

print(
    "335000 ->",
    paye.calculate(335000)
)

print(
    "335001 ->",
    paye.calculate(335001)
)

print(
    "410000 ->",
    paye.calculate(410000)
)

print(
    "485000 ->",
    paye.calculate(485000)
)

print(
    "10000000 ->",
    paye.calculate(10000000)
)
