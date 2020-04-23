# make predictions based on the parameters
# obtained through logistic regression

import json
from hyp import hypothesis

filename = "parameters.json"
with open(filename) as f:
    theta = json.load(f) # list storing the parameters

print("Enter the input features, one by one, separated by newlines.")
print("Example: ")
print("2")
print("3")
x = [1] # stores the input features plus x_0 = 1
for i in range(1, len(theta)):
    x.append(float(input()))

h = hypothesis(theta, x)
print(f"y = {1 if (h >= 0.5) else 0}")
