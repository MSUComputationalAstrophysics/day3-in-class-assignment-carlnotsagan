'''
Short code to create data points for experimentation with interpolation techniques.
The end result are arrays of values for x and f(x), with a user-defined number of
samples (nsample) over a user-chose interval (xstart to xend).
'''

import numpy as np
import random as rand


def analytic_func(x):
    # function that generates our f(x) values
    return np.sin(1.3*x)**2 + 1.0*(np.cos(5.0*x-0.7)-0.5) + 0.2*np.exp(0.2*x) + (0.1*x)**3

# set the random seed by hand to make sure everybody gets the same points.
# use this seed because your professor is old and easily amused.
rand.seed(8675309)

# will result in approximately nsample samples at the end, spread over
# interval defined by xstart, xend
xstart = -20.0
xend = 20.0
nsample = 100

# needed to determine the mean distance between adjacent points
dx = (xend-xstart)/nsample

# lists to temporarily hold x, f(x) values
all_x = []
all_f_of_x = []

thisx = xstart

'''
Loops from xstart to (approximately) xend, calculating f(x) values as we go.
We then step forward in x by some random distance between 0 and 2*dx until
we reach the end of our interval.
'''
while(thisx <= xend):
    
    thisy = analytic_func(thisx)
    
    all_x.append(thisx)
    all_f_of_x.append(thisy)
    
    thisx += 2.0*dx*rand.random()

# we wind up with some arrays that you can use for your nefarious purposes.
all_x = np.array(all_x)
all_f_of_x = np.array(all_f_of_x)

