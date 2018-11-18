#!~/.brew/bin/python
import sys
import csvTools as csv
import mathTools as math
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def main():
	if len(sys.argv) == 2:
		datas = csv.readCSVFile(sys.argv[1], ',')
		if (datas is None):
			sys.exit(1)
		subjectDatas = csv.dropUselessColumn(datas, False)
		if (subjectDatas is None):
			sys.exit(1)
		# subjectNames, subjectsByHouse = csv.getSubjectValueByHouse(datas)
		# size = len(subjectNames)
		# sqrtSize = math.sqrt(size)
		# sqrtSize = int(sqrtSize) if (sqrtSize == int(sqrtSize)) else int(sqrtSize + 1)
		# elements = []
		area = np.pi*3

		# plt.plot(subjectsByHouse[0], subjectsByHouse[1], s=area, c=csv.colors[0], alpha=0.5)
		# print subjectsByHouse[0][0]
		# plt.scatter(subjectsByHouse[0], subjectsByHouse[1], s=area, c=csv.colors, alpha=0.5)
		# plt.scatter([[0,1],[1,2],[2,3,4,5],[3,2,1]], [[0,1],[1,2],[2,2,3,4],[3,1,2]], s=area, c=csv.colors, alpha=0.5)
		# plt.title('Scatter plot pythonspot.com')
		# plt.xlabel('x')
		# plt.ylabel('y')
		sns.relplot(x="Astronomy", y="Defense Against the Dark Arts", hue="Hogwarts House", hue_order=csv.houseNames, palette=csv.colors, data=subjectDatas)
		# for subjectIndex in range(size):
		# 	elements.append(fig.add_subplot(4,4,subjectIndex + 1))
		# 	for houseIndex in range(len(subjectsByHouse[subjectIndex])):
		# 		elements[subjectIndex].plot(subjectsByHouse[subjectIndex][houseIndex], label=houseNames[houseIndex], color=colors[houseIndex], kind='scatter')
		# 	elements[subjectIndex].set_title(subjectNames[subjectIndex])
		# 	elements[subjectIndex].legend()
		plt.show()
	else:
		print 'Error script : python scatter_.py file.'

if __name__ == "__main__":
	main()