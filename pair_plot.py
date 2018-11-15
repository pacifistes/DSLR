#!~/.brew/bin/python
import tools
import sys
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def main():
	if len(sys.argv) == 2:
		datas = tools.readCSVFile(sys.argv[1], ',')
		if (datas is None):
			sys.exit(1)
		print datas
		# subjectDatas = tools.getSubjectDatas(datas)
		subjectDatas = tools.getSubjectDatasWithHouse(datas)
		if (subjectDatas is None):
			sys.exit(1)
		subjectDatas = subjectDatas.dropna()
		
		# print subjectDatas
		sns.pairplot(subjectDatas, hue="Hogwarts House")
		plt.show()
		
		# sns.pairplot(subjectDatas)
	else:
		print 'Error script : python pair_plot.py file.'

if __name__ == "__main__":
	main()