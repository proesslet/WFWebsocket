import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read in data from txt/csv file
data = pd.read_csv('tempest.txt', names=['type','utc','local','temp'])

# Plot temp data with local timestamp
plt.plot(data['local'], data['temp'])
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Tempest Temperature')
plt.show()

