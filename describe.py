#!~/.brew/bin/python
import csvTools as csv
import mathTools as math
import pandas as pd
import sys

def describeColumn(values):
	return [math.count(values), math.mean(values), math.std(values), math.minimum(values), math.quart(values), math.half(values), math.treeQuarts(values), math.maximum(values)]

def describe(datas):
	dictDescribeData = {}
	indexNames = {0 : "count", 1 : "mean", 2 : "std", 3 : "min", 4 : "25%", 5 : "50%", 6 : "75%", 7 : "max"}
	for data in datas:
		dictDescribeData.update({data : describeColumn(datas[data].values)})
	describeDatas = pd.DataFrame(dictDescribeData)
	describeDatas.rename(index = indexNames, inplace = True)
	return describeDatas

def main():
	if len(sys.argv) == 2:
		datas = csv.readCSVFile(sys.argv[1], ',')
		if (datas is None):
			sys.exit(1)
		subjectDatas = csv.dropUselessColumn(datas, True)
		if (subjectDatas is None):
			sys.exit(1)
		# print subjectDatas.describe()
		# print "\n"
		print describe(subjectDatas)
	else:
		print 'Error script : python describe.py file.'

if __name__ == "__main__":
	main()
