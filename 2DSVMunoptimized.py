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
fig = plt.subplot()
fig.set_xlim(0,3)
fig.set_ylim(0,3)
for i in data:
	for j in data[i-1]:
		fig.scatter(j[0],j[1])

plt.show()

