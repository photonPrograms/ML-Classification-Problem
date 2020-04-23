# assuming that there are only two independent features (x1, x2)
# say representing the coordinates of a point in a battle zone
# and a binary label, say the presence or absence of a landmine
# plot (x1, x2) with corresponding labels
# hence plot the line separating the classification regions

import matplotlib.pyplot as plt
import json

filename = "training_set.json"
with open(filename) as f:
    training_set = json.load(f)

x1_0, x2_0, x1_1, x2_1 = [], [], [], []
for i in range(0, len(training_set["coordinates"])):
    if (training_set["verdict"][i]):
        x1_1.append(training_set["coordinates"][i][0])
        x2_1.append(training_set["coordinates"][i][1])
    else:
        x1_0.append(training_set["coordinates"][i][0])
        x2_0.append(training_set["coordinates"][i][1])

fig, ax = plt.subplots()
ax.scatter(x1_0, x2_0, c = "blue", label = "y = 0")
ax.scatter(x1_1, x2_1, c = "red", label = "y = 1")
ax.legend()

minx1, maxx1 = x1_0[0], x1_0[1]
for x1 in x1_0:
    if x1 < minx1:
        minx1 = x1
    if x1 > maxx1:
        maxx1 = x1
for x1 in x2_0:
    if x1 < minx1:
        minx1 = x1
    if x1 > maxx1:
        maxx1 = x1

x1, x2 = [minx1, maxx1], []

filename = "parameters.json"
with open(filename) as f:
    theta = json.load(f)

for x in x1:
    x2.append(-theta[1]/theta[2]*x - theta[0]/theta[2])
ax.plot(x1, x2, color = "green")

plt.show()
