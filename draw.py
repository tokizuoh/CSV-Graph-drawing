#%%
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()
sns.set_context("poster")
from matplotlib import pyplot as plt
%matplotlib inline
from datetime import datetime

df = pd.read_csv("--path--", index_col=0, parse_dates=True)
ax = df.groupby("Date").max().plot(color = "r", figsize = (12, 9))
df.groupby("Date").mean().plot(ax = ax, color = "g")
df.groupby("Date").min().plot(ax = ax, color = "b")
ax.legend(["maxi", "mean", "mini"])
plt.subplots_adjust(bottom = 0.2)

plt.title("Obihiro Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature [°C]")
ax.grid(which = "both")
ax.grid(which="minor", color = "white")

plt.grid(which="major", color = "white", linestyle = "--")
plt.grid(which="minor", color = "white", linestyle = "--")

plt.savefig("test.PNG")
plt.show()
