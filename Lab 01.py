import matplotlib.pyplot as plt
import pandas as pd

charging = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-354-Lab-01\rc data - charging.csv')
discharging = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-354-Lab-01\rc data - discharging.csv')

X_1 = charging.iloc[:, 0]
Y_1 = charging.iloc[:, 1]

X_2 = discharging.iloc[:, 0]
Y_2 = discharging.iloc[:, 1]

fig = plt.figure(dpi=300)
plt.scatter(X_1, Y_1, label=(r'Charging'))
plt.scatter(X_2, Y_2, label=(r'Discharging'))
    
plt.title('RC Circuit')
plt.xlabel(r'Time (s)')
plt.ylabel(r'Voltage (V)')
plt.legend()

fig.savefig('rc plot.png')