from math import log
from hyp import hypothesis

def costfunc(X, y, theta):
    """
    for the matrix X and vector y and parameters theta
    compute the cost function in logisic regression
    """
    m, s = len(y), 0
    for i in range(0, m):
        s -= indiv_cost(X[i], y[i], theta)
    return s / m

def indiv_cost(x_i, y_i, theta):
    """
    in the summation for cost function
    find the cost contribution from each element vector x_i and scalar y_i
    in the training set
    """
    h = hypothesis(theta, x_i)
    return (y_i * log(h) + (1 - y_i) * log(1 - h))
