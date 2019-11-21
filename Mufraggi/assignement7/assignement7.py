def fixedMonthlyPayment(P, r, n):
   top = (1 + r)**n
   bot = ((1 +r)**n) - 1
   res_top_bot = top / bot
   return P * r * res_top_bot


def OutstandingLoanBalance(P, r, n, m):
    top = ((1 + r)**n) - ((1 + r)**m)
    bot = ((1 + r)**n) - 1
    res_top_bot = top/bot
    return P * res_top_bot


print("Can you give me the value of Principal?")
P = float(input())
print("Can you give me the value of mounthly floaterest rate?")
r = float(input()) / 100
print("Can you give me the value of number of months?")
n = float(input())
print("Can you give me the value of M")
m = float(input())

FMP = fixedMonthlyPayment(P, r, n)
OLB = OutstandingLoanBalance(P, r, n, m)

print("Fixed Monthly Payment", FMP)
print("Outsanding Loan Balance", OLB)

