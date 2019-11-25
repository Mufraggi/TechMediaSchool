#!/usr/bin/env python3

from sys import argv

def calculateFuture(v, r, n):
    return v * (1 + r) ** n

def calculatePresent(v, r, n):
    return v / ((1 + r) ** n)

if __name__ == "__main__":
    try:
        p = argv[1]
        assert(p ==  'future' or p == 'present')
        v = float(input(f"Enter the {'present' if p == 'future' else 'future'} value\n"))
        r = float(input("Enter the rate\n"))
        n = float(input("Enter the number of years\n"))
        value = 0
        if p == 'future':
            value = calculateFuture(v,r,n)   
        else:
            value = calculatePresent(v,r,n)
        print(f"{value:.2f}")
    except IndexError:
        print("Parameter should be specified (<future> or <present>)")
        exit(1)
    except AssertionError:
        print("Please enter a <future> or <present> parameter")
        exit(1)