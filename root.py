'''
Functions for root-finding.  Each of these functions takes in an argument
x and returns f(x).
'''

import numpy as np

def f1(x):
    # should be an easy one to determine roots
    # roots are (exactly):  +2.5, -8.7, -1.2
    return (x-2.5)*(x+8.7)*(x+1.2)

def f2(x):
    # somewhat harder to determine the root
    # root is (approximately): -3.0943512729560467
    return (0.2*np.sin(2.0*x)+0.6) + 0.2*x

def f3(x):
    # good luck! this will kill many root-finders.  MWUHAHAHA.
    # roots are (approximately): 3.1240484736455802, 3.6352284118019034
    return (np.sin(2.0*(x-4))+0.6) + 0.5*(x-4)**2

