#!/usr/bin/env python3

try:
    p = float(input("Principal ?\n"))
    r = float(input("Monthly interest rate ?\n")) / 100
    n = int(input("Number of months ?\n"))
    m = int(input("Number of M ?\n"))
except ValueError:
    print("Please enter a valid number format !")
    exit(1)

fixed = p * r * (((1 + r) ** n) / (((1 + r) ** n) - 1))
balance = p * ((((1 + r) ** n) - ((1 + r) ** m)) / (((1 + r) ** n) - 1))
print("=" * 10)
print(f"${fixed:.2f} monthly payment.")
print(f"${balance:.2f} outstanding balance.")