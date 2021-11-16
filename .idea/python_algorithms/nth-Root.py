# -*- coding: utf-8 -*-
"""
Project name: FABNITIN Calculator
Created: 11/16/2021
Assignee: FibSchub
"""


# Calculate the nth root of a given non-negative number a
# nth Root of a is solution of equation f(z) = 0, with f(z) = z**n - a
# Use Newton's method to approximate solution of f(z) = 0



def nRootNewton (a, n, x):
    # a: Number of which the root gets calculated
    # n: nth root
    # x: Current approximation of the nth root of a
    
    # Calculation of the recursion step
    xnew = (n-1)/n * x + a/(n*x**(n-1))
    
    # Approximate solution of f(x) = 0 which fulfills f(x) <= error should
    # be good enough
    error = 10**-10
    
    if abs(xnew**n - a) <= error:
        return xnew
    
    # Executing the recursion step
    else:
        return nRootNewton(a, n, xnew)




def nRoot (a, n=2):
    
    # Absorbing infinities
    if n == 0:
        print("division by zero")
        pass
    
    # Absorbing negative numbers
    elif a <= 0:
        print(a, "is a negaive number")
        pass
    
    elif a == 0:
        return 0
    
    # xstart is initial value to start the recursion algorithm
    else:
        xstart = (a-1)/(2*n) + 1/2
        
        # Executing Newton's method
        return nRootNewton(a, n, xstart)