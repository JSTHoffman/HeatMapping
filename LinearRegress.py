import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# df = pd.read_csv(r'C:\Users\SUST heavyweight\Desktop\daymedlst_ndvi.csv')
# x = np.array(df['GRID_CODE'])
# y = np.array(df['GRID_COD_1'])

df = pd.read_csv(r'T:\JHoffman\Summer\NDVI\Sample_DayLST_NDVI.csv')
# df = df[df.day_medlst > 297.2]
# df = df[df.medNDVI > -0.1]
df = df[df.day_medlst != 0]
df = df[df.medNDVI != 0]

x = np.array(df['day_medlst'])
y = np.array(df['medNDVI'])

fig, ax = plt.subplots()
fit = np.polyfit(x, y, deg=1)
ax.plot(x, fit[0] * x + fit[1], color='red')
ax.scatter(x, y)

plt.title('LST vs. NDVI')
plt.xlabel('Daytime Median Surface Temperature (K)')
plt.ylabel('NDVI')

r = np.corrcoef(x, y)[0, 1]
print 'R^2 = {0}'.format(r**2)
plt.show()

print '\nEnd of script.'
