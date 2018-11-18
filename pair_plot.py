#!~/.brew/bin/python
import csvTools as csv
import mathTools as math
import sys
import seaborn as sns
import matplotlib.pyplot as plt

def main():
	if len(sys.argv) == 2:
		datas = csv.readCSVFile(sys.argv[1], ',')
		if (datas is None):
			sys.exit(1)
		subjectDatas = csv.dropUselessColumn(datas, False)
		if (subjectDatas is None):
			sys.exit(1)
		subjectDatas = subjectDatas.dropna()
		replacements = {data : data[:4] for data in subjectDatas if data != 'Hogwarts House'}
		g = sns.pairplot(subjectDatas, hue="Hogwarts House", hue_order=csv.houseNames, palette=csv.colors, height=1.5, plot_kws={"s": 5})
		# g = sns.pairplot(subjectDatas, hue="Hogwarts House", hue_order=csv.houseNames, palette=csv.colors, height=1.5, plot_kws={"s": 5}, diag_kind='hist', diag_kws={"alpha":0.5})
		size = len(subjectDatas.columns) - 1
		for i in range(size):
			for j in range(size):
				xlabel = g.axes[i][j].get_xlabel()
				ylabel = g.axes[i][j].get_ylabel()
				if xlabel in replacements.keys():
					g.axes[i][j].set_xlabel(replacements[xlabel])
				if ylabel in replacements.keys():
					g.axes[i][j].set_ylabel(replacements[ylabel])
		plt.show()
	else:
		print 'Error script : python pair_plot.py file.'

if __name__ == "__main__":
	main()