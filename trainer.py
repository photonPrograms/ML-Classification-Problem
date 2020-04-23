# get the parameters for a classification hypothesis
# using logistic regression with gradient descent

import json
from hyp import hypothesis
from cost import costfunc

def descent(X, y, theta, j):
    """calculate the updation for theta_j for gradient descent"""
    s = 0
    for i in range(0, m):
        s += (hypothesis(theta, X[i]) - y[i]) * X[i][j]
    return s

filename = "training_set.json" # json file with the training set
with open(filename) as f:
    training_set = json.load(f)

X = [] # the training set coordinates/features including x_0 = 0
y = [] # the training set labels
m = len(training_set["coordinates"]) # number of examples

for i in range(0, m):
    X.append(training_set["coordinates"][i])
    X[i].insert(0, 1)
    y.append(training_set["verdict"][i])

theta = [] # parameters for the hypothesis
for i in range(0, len(X[0])):
    theta.append(0)

alpha = 0.01 # learning rate
niter = 100000 # number of iterations in gradient descent to get theta
cost_list = [] # store cost function after each iteration

for k in range(0, niter):
    # update theta in gradient descent
    temp = theta[:]
    for j in range(0, len(theta)):
        temp[j] = theta[j] - alpha / m * descent(X, y, theta, j)
    theta = temp[:]

    # compute the cost function in each iteration
    cost_list.append(costfunc(X, y, theta))

filename = "parameters.json"
with open(filename, "w") as f:
    json.dump(theta, f)

filename = "costs.json"
with open(filename, "w") as f:
    json.dump(cost_list, f)
