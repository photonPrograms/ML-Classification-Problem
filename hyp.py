# the hypothesis function giving probability that y = 1

from math import exp

def sigmoid(z):
    """compute the sigmoid function for a real number z"""
    return 1 / (1 + exp(-z))

def hypothesis(theta, x):
    """compute the hypothesis for parameters theta and features x"""
    s = 0   
    for i in range(0, len(x)):
        s += theta[i] * x[i]
    return sigmoid(s)
