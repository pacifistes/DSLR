#!~/.brew/bin/python
import sys
import csvTools as csv
import mathTools as math
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
	vlen = len(sys.argv)
	if (vlen == 2 or (vlen == 3 and sys.argv[1] == "-all")):
		datas = csv.readCSVFile(sys.argv[vlen - 1], ',')
		if (datas is None):
			sys.exit(1)
		subjectDatas = csv.dropUselessColumn(datas, False)
		if (subjectDatas is None):
			sys.exit(1)
		subjectNames, subjectsByHouse = csv.getSubjectValueByHouse(datas)
		fig = plt.figure()
		elements = []
		size = len(subjectNames)
		sqrtSize = math.sqrt(size)
		sqrtSize = int(sqrtSize) if (sqrtSize == int(sqrtSize)) else int(sqrtSize + 1)
		if (vlen == 3):
			for subjectIndex in range(size):
				elements.append(fig.add_subplot(sqrtSize,sqrtSize,subjectIndex + 1))
				elements[subjectIndex].hist(subjectsByHouse[subjectIndex], label=csv.houseNames, color=csv.colors)
				elements[subjectIndex].set_title(subjectNames[subjectIndex])
				elements[subjectIndex].legend()
		else:
			elements.append(fig.add_subplot(1,1,1))
			elements[0].hist(subjectsByHouse[10], label=csv.houseNames, color=csv.colors)
			elements[0].set_title(subjectNames[10])
			elements[0].legend()
		plt.show()
	else:
		print 'Error script : python histogram.py [-all] file.'

if __name__ == "__main__":
	main()