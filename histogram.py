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
		for subjectIndex in range(size):
			elements.append(fig.add_subplot(4,4,subjectIndex + 1))
			elements[subjectIndex].hist(subjectsByHouse[subjectIndex], label=houseNames, color=colors)
			elements[subjectIndex].set_title(subjectNames[subjectIndex])
			elements[subjectIndex].legend()
			# print subjectsByHouse[subjectIndex]
			# plt.hist(subjectsByHouse[subjectIndex], label=houseNames)
		plt.show()
	else:
		print 'Error script : python pair_plot.py file.'

if __name__ == "__main__":
	main()