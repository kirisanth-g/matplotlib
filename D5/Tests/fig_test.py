import matplotlib.pyplot as plt

n = plt.figure("fig 1")
o = plt.figure("fig 2")

ax1 = plt.subplot2grid((3,3),(0,0))
ax2 = plt.subplot2grid((3,3),(0,1), colspan=2)
ax3 = plt.subplot2grid((3,3),(1,2), rowspan=2)
ax4 = plt.subplot2grid((3,3),(2,0))
plt.show()
