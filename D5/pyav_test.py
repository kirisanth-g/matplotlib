import matplotlib.pyplot as plt

h = plt.figure()
plt.axhline(2, 0, 10)
v = plt.figure()
plt.axvline(2, 0, 10)

h.pyav_addtomovie()
v.pyav_addtomovie()

plt.make_movie('work.mp4', '1/2')
