#!~/.brew/bin/python
from __future__ import division
import tools
import sys
import pandas as pd
import numpy as np


def count(values):
	return np.count_nonzero(~np.isnan(values))

def mean(values):
	sum = 0.00
	for value in values:
		if (~np.isnan(value)):
			sum += value
	return sum/count(values)

def std(values):
	return 2.00

def minimum(values):
	min = None
	for value in values:
		if (~np.isnan(value)):
			if (min is None):
				min = value
			elif (value < min):
				min = value
	return min

def maximum(values):
	max = None
	for value in values:
		if (~np.isnan(value)):
			if (max is None):
				max = value
			elif (value > max):
				max = value
	return max

def percentile(values, percentile):
	number = int(percentile * count(values))
	index = 0
	for value in values:
		if (index == number):
			return values[index]
		if (~np.isnan(value)):
			index += 1
	return 0

def quart(values):
	return percentile(values, 0.25)

def half(values):
	return percentile(values, 0.5)

def treeQuarts(values):
	return percentile(values, 0.75)

def describeColumn(values):
	return [count(values), mean(values), std(values), minimum(values), quart(values), half(values), treeQuarts(values), maximum(values)]

def describe(datas):
	dictDescribeData = {}
	indexNames = {0 : "count", 1 : "mean", 2 : "std", 3 : "min", 4 : "25%", 5 : "50%", 6 : "75%", 7 : "max"}
	for data in datas:
		dictDescribeData.update({data : describeColumn(datas[data].values)})
	describeDatas = pd.DataFrame(dictDescribeData)
	describeDatas.rename(index = indexNames, inplace = True)
	print describeDatas

def main():
	if len(sys.argv) == 2:
		dataDic = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 'year': [2012, 2012, 2013, 2014, 2014], 'reports': [4, 24, 31, 2, 3]}
		datas = tools.readCSVFile(sys.argv[1], ',')
		if (datas is None):
			sys.exit(1)
		subjectDatas = tools.getSubjectDatas(datas)
		if (subjectDatas is None):
			sys.exit(1)
		describe(subjectDatas)
	else:
		print 'Error script : python describe.py file.'


if __name__ == "__main__":
	main()
