# -*- coding: utf-8 -*-
"""
Project name: FABNITIN Calculator
Created: 11/16/2021
Assignee: FibSchub
"""

def nRootNewton (a, n, x):
    xnew = (n-1)/n * x + a/(n*x**(n-1))
    error = 10**-10
    
    if abs(xnew**n - a) <= error:
        return xnew
    
    else:
        return nRootNewton(a, n, xnew)




def nRoot (a, n=2):
    
    if n == 0:
        print("division by zero")
        pass
    
    elif a == 0:
        return 0
    
    else:
        xstart = (a-1)/(2*n) + 1/2
        return nRootNewton(a, n, xstart)