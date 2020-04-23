# plotting the variation of cost function with the number of iterations
# to see whether logistic regression is working as expected

import matplotlib.pyplot as plt
import json

filename = "costs.json"
with open(filename) as f:
    cost_list = json.load(f)

iterations =  range(1, len(cost_list) + 1)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(iterations, cost_list, linewidth = 2, color = "red")
ax.set_title("Cost Function Variation in Gradient Descent", fontsize = 20)
ax.set_xlabel("# of Iterations", fontsize = 10)
ax.set_ylabel("Cost Function", fontsize = 10)
ax.tick_params(axis = "both", labelsize = 10)

plt.show()
