import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import sys
style.use("dark_background")


class mySVC:
	def __init__(self):
		print("Hello, left click for a +, right click for an x")
		self.data = {'-1':np.array([[1,1]]), '1':np.array([[2,2]])}
		self.fig = plt.figure()
		self.ax = plt.subplot(1,1,1)
		self.ax.set_xlim(0,3)
		self.ax.set_ylim(0,3)
		self.cid = self.fig.canvas.mpl_connect('button_press_event', self)
		for key, value in self.data.items():
			if (key == "-1"):
				k = "x"
				col = "red"	
			if (key == "1"):
				k = "+"
				col = "green"
			for i in value:
				self.ax.scatter(i[0],i[1], s=100, color=col, marker=k)

	def __call__(self, event):
		if event.button == 1:
			self.data['1'] = np.array([[event.xdata,event.ydata]] + list(self.data['1']))
			self.ax.scatter(event.xdata, event.ydata, s=100, color="green", marker="+")
		if event.button == 3:
		        self.data['-1'] = np.array([[event.xdata,event.ydata]] + list(self.data['-1']))
			self.ax.scatter(event.xdata, event.ydata, s=100, color="red", marker="x")
		self.fig.canvas.draw()

	def fit(self, data):
		pass
	def predict(self, data):
		#group = self.w
		pass 

	


	
#######################TEST PRINT GRAPH
newsvm = mySVC()

plt.show()

