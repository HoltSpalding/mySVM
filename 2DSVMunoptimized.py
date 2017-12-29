import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")


class mySVC:
	def __init__(self):
		print("Hello")

	def fit(self, data):
		pass
	def predict(self, data):
		pass



#######################TEST PRINT GRAPH
newsvm = mySVC()
data = np.array([[1,1],[2,2]])
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim(0,3)
ax.set_ylim(0,3)


def onclick(event):
	ax.scatter(event.xdata, event.ydata)
	plt.draw()
	
cid = fig.canvas.mpl_connect('button_press_event', onclick)


for i in data:
	for j in data[i-1]:
		ax.scatter(j[0],j[1])

plt.show()

