### Imports
import numpy as np

# This function computes the first derivative of a single variable 
# function using the: 
# two-point method given in equation (3.4) of Pang, (points = 2)
# three-point method given in equation (3.6) of Pang, (points = 3) DEFAULT
# or the five-point method given in equation (3.9) of Pang, (points = 5).
#
# The function takes in as arguments:
# f(x) - a user defined single variable function
# X - the single point at which the derivative shold be evaluated
# h - a user defined step size
# points - the number of the evaluation points in a given method
#
# Returns: value of first derivative evaluated at X

def first_derivative(f,X,h,points=3):
    function = f
    if points==2:
        prime_function_two_point = (function(X+h)-function(X))/(h)
        return prime_function_two_point
    elif points==3:
        prime_function_three_point = (function(X+h)-function(X-h))/(2*h)
        return prime_function_three_point
    elif points==5:
        prime_function_five_point = ((1.)/(12.*h))*(function(X-2.*h)-8.*function(X-h)+8.*function(X+h)-function(X+2.*h))
        return prime_function_five_point
    else:
        print('Sorry please specify either the two,three, or five- point method to compute the derivative.')

