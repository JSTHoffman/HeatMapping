import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\SUST heavyweight\Desktop\daymedlst_ndvi.csv')

x = df['GRID_COD_1']
y = df['GRID_CODE']

fig, ax = plt.subplots()
fit = np.polyfit(x.value.flatten(), y.values.flatten, deg=1)
ax.plot(x, fit[0] * x + fit[1], color='red')
ax.scatter(x, y)

print fig
print fit