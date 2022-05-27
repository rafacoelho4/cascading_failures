import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# panda reading files
a = pd.read_csv('./metrics/p_data.csv', index_col=0)
b = pd.read_csv('./metrics/p_failsize1495.csv', index_col=0)
# b = pd.read_csv('./size_output/p_failsize_phi04_it10000.csv', index_col=0)

# getting all variables
degree = np.array([])
betweenness = np.array([])
closeness = np.array([])
fail = np.array([])

# iterating dataframe
i = 0
while i < 1495:
    degree = np.append(degree, a.values[i][0])
    betweenness = np.append(betweenness, a.values[i][1])
    closeness = np.append(closeness, a.values[i][2])
    fail = np.append(fail, b.values[i][0])
    i = i + 1

# joining all arrays
all = [fail, degree, betweenness, closeness]

# calculating pearson correlation
rho = []
rho.append(np.corrcoef(degree, fail))
rho.append(np.corrcoef(betweenness, fail))
rho.append(np.corrcoef(closeness, fail))

# plotting
label = ["fail size", "degree", "betweenness", "closeness"]
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 3))
for i in [0, 1, 2]:
    ax[i].scatter(all[i + 1], all[0])
    ax[i].set_title("rho = " + str("{:.4f}".format(rho[i][0][1])))
    ax[i].set(xlabel=label[i + 1], ylabel=label[0])
    # calculate equation for trendline
    z = np.polyfit(all[i + 1], all[0], 1)
    p = np.poly1d(z)
    # add trendline to plot
    ax[i].plot(all[i + 1], p(all[i + 1]), "r--")
fig.subplots_adjust(wspace=.4)
plt.show()
