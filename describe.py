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
		if (data == 'Hogwarts House'):
			continue
		dictDescribeData.update({data : describeColumn(datas[data].values)})
	describeDatas = pd.DataFrame(dictDescribeData)
	describeDatas.rename(index = indexNames, inplace = True)
	return describeDatas

def main():
	vlen = len(sys.argv)
	if (vlen == 2 or (vlen == 3 and sys.argv[1] == "-byHouse")):
		datas = csv.readCSVFile(sys.argv[vlen - 1], ',')
		if (datas is None):
			sys.exit(1)
		subjectDatas = csv.dropUselessColumn(datas, False)
		if (subjectDatas is None):
			sys.exit(1)
		# print subjectDatas.describe()
		print "Describe general:\n{}\n".format(describe(subjectDatas))
		if (vlen == 3):
			for house in csv.houseNames:
				print "Describe {}:\n{}\n".format(house, describe(subjectDatas.loc[subjectDatas['Hogwarts House'].isin({house})]))

	else:
		print 'Error script : python describe.py -byHouse file.'

if __name__ == "__main__":
	main()
