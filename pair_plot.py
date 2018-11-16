#!~/.brew/bin/python
import tools
import sys
import seaborn as sns
import matplotlib.pyplot as plt

def main():
	if len(sys.argv) == 2:
		datas = tools.readCSVFile(sys.argv[1], ',')
		if (datas is None):
			sys.exit(1)
		subjectDatas = tools.getSubjectDatasWithHouse(datas)
		if (subjectDatas is None):
			sys.exit(1)
		subjectDatas = subjectDatas.dropna()
		replacements = {data : data[:4] for data in subjectDatas if data != 'Hogwarts House'}
		houseNames = ['Slytherin', 'Hufflepuff', 'Gryffindor', 'Ravenclaw']
		colors = ["#33c47f", "#A061D1", "#FF6950", "#4180db"]
		g = sns.pairplot(subjectDatas, hue="Hogwarts House", hue_order=houseNames, palette=colors, height=1.5, plot_kws={"s": 5})
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