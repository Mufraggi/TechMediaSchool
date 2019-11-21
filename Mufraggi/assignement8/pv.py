def pv(r, n, fv):
    before_multiplication = (1 + r)**n
    return fv /before_multiplication


print("enter the future value ")
fv = float(input())
print("enter the rate")
r = float(input())
print(" enter the number of years")
n = float(input())

print(pv(r, n, fv))

