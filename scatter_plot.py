#!~/.brew/bin/python
import tools
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
	if len(sys.argv) == 2:
		datas = tools.readCSVFile(sys.argv[1], ',')
		if (datas is None):
			sys.exit(1)
		subjectDatas = tools.getSubjectDatasWithHouse(datas)
		if (subjectDatas is None):
			sys.exit(1)
		subjectNames, subjectsByHouse, houseNames, colors = tools.getSubjectValueByHouse(datas)
		size = len(subjectNames)
		sizesqrt = tools.sqrt(size)
		fig = plt.figure()
		elements = []
		area = np.pi*3

		plt.scatter(subjectsByHouse[0], subjectsByHouse[1], s=area, c=colors[0], alpha=0.5)
		plt.title('Scatter plot pythonspot.com')
		plt.xlabel('x')
		plt.ylabel('y')
		# for subjectIndex in range(size):
		# 	elements.append(fig.add_subplot(4,4,subjectIndex + 1))
		# 	for houseIndex in range(len(subjectsByHouse[subjectIndex])):
		# 		elements[subjectIndex].plot(subjectsByHouse[subjectIndex][houseIndex], label=houseNames[houseIndex], color=colors[houseIndex], kind='scatter')
		# 	elements[subjectIndex].set_title(subjectNames[subjectIndex])
		# 	elements[subjectIndex].legend()
		plt.show()
	else:
		print 'Error script : python pair_plot.py file.'

if __name__ == "__main__":
	main()