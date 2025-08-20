import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


sns.set_style("whitegrid")
sns.set_context("talk")


np.random.seed(42)
hours = [f"{h}:00" for h in range(8, 22)] 
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


data = np.random.poisson(lam=5, size=(len(hours), len(days))).astype(float)
data[10:14, :] += np.random.randint(5, 15, size=(4, len(days))) 
data[:, -2:] += np.random.randint(5, 20, size=(len(hours), 2))   


df = pd.DataFrame(data, index=hours, columns=days)


plt.figure(figsize=(8, 8))
ax = sns.heatmap(df, cmap="YlGnBu", annot=True, fmt=".0f", linewidths=0.5, cbar_kws={'label': 'Engagement Score'})


plt.title("Customer Engagement Patterns\nby Weekday and Hour", fontsize=16, pad=20)
plt.xlabel("Day of Week")
plt.ylabel("Hour of Day")


plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
