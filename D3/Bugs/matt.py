import matplotlib.pyplot as plt
import numpy as np
a = np.random.rand(10,1)

plt.plot(a, label='label')
legend = plt.legend()
frame = legend.get_frame()
frame.set_facecolor('green')
plt.show()


import seaborn as sns

plt.plot(a, label='label')
legend = plt.legend()
frame = legend.get_frame()
frame.set_facecolor('green')
plt.show()
