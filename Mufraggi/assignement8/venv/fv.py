def fv(r, n, pv):
    before_multiplication = (1 + r)**n
    return before_multiplication * pv


print("enter the present value")
pv = float(input())
print("enter the rate")
r = float(input())
print(" enter the number of years")
n = float(input())

print(fv(r, n, pv))

