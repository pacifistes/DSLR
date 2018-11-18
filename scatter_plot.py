#!~/.brew/bin/python
import sys
import csvTools as csv
import mathTools as math
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
		sns.relplot(x="Astronomy", y="Defense Against the Dark Arts", hue="Hogwarts House", hue_order=csv.houseNames, palette=csv.colors, data=subjectDatas)
		plt.show()
	else:
		print 'Error script : python scatter_.py file.'

if __name__ == "__main__":
	main()