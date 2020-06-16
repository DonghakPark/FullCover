import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("./GAS_DATASET.csv")
X = data["TIMESTEMP"]
Y = data["GAS_DATA"]

# line_fitter = LinearRegression()
plt.plot(Y,'o')
plt.xlabel("time(ms)")
plt.ylabel("Gas_data")

plt.axhline(y = 250, color = "r", linewidth = 2)
plt.show()

