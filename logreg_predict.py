#!~/.brew/bin/python
from __future__ import division
import math as m
import sys
import csvTools as csv
import mathTools as math

def	sigmoid(value):
	return 1 / (1 + (m.e ** -value))

def h(thetas, values):
	result = 0.0
	for i in range(len(thetas)):
		result += (thetas[i] * values[i])
	return sigmoid(result)

def normalize(subjectDatas):
	for subject in subjectDatas:
		if (subject == 'Hogwarts House'):
			continue
		values = subjectDatas[subject].values
		xmin = math.minimum(values)
		xmax = math.maximum(values)
		for i in range(len(subjectDatas[subject].values)):
			subjectDatas.loc[[i], [subject]] = (subjectDatas[subject][i] - xmin) / (xmax - xmin)
	return subjectDatas

def predict_all(thetas, datasTest):
	houseNames = ['Ravenclaw','Slytherin','Gryffindor','Hufflepuff']
	print(datasTest)
	print(datasTest.shape[0])
	print(datasTest.iloc[0])
	result = []
	for line in range(datasTest.shape[0]):
		predict = []
		for i in range(len(houseNames)):
			predict.append(h(thetas.iloc[i], datasTest.iloc[line]))
		result.append([houseNames[predict.index(max(predict))]])
	return result

def main():
	vlen = len(sys.argv)
	if (vlen == 2):
		thetas = csv.readCSVFile('thetas.csv', ',')
		datasTest = csv.readCSVFile("resources/dataset_test.csv", ',')
		if (datasTest is None):
			sys.exit(1)
		datasTest = csv.dropColumns(datasTest, csv.ignoredSubjects)
		if (datasTest is None):
			sys.exit(1)
		datasTest.drop('Hogwarts House', axis=1, inplace=True)
		datasTest = normalize(datasTest)
		result = predict_all(thetas, datasTest.dropna().reset_index(drop=True))
		csv.writeCSVFile('result.csv', result)
	else:
		print("Error script : python logreg_train.py file.")
if __name__ == "__main__":
	main()