#!~/.brew/bin/python
from __future__ import division
import math as m
import sys
import csvTools as csv
import mathTools as math

# Function sigmoid
# Params : (Float) value
# Return : reader a value between 0 and 1
def	sigmoid(value):
	return 1 / (1 + (m.e ** -value))

def h(thetas, values):
	result = 0.0
	for i in range(len(thetas)):
		result += (thetas[i] * values[i])
	return sigmoid(result)

def costFunction(houseColumns, subjectColumns, thetas, house, size):
	cost = 0
	for line in range(subjectColumns.shape[0]):
		y = 0
		if (houseColumns.iloc[line] == house):
			y = 1
		xSigmoid = h(thetas, subjectColumns.iloc[line])
		cost = cost + (y * m.log10(xSigmoid) + (1 - y) * m.log10(1 - xSigmoid))
	return (-1 / size) * cost

def	minimizeCostFunction(houseColumns, subjectColumns, thetas, learningRate, size, nbr_house, nbr_subject, houseNames):
	for i, house in zip(range(nbr_house), houseNames):
		for subject, i_subject in zip(subjectColumns.columns, range(nbr_subject)):
			thetas[i][i_subject] -= ((learningRate / size) * costFunction(houseColumns, subjectColumns,thetas[i], house, size))
	return thetas

def	train_prediction(datas):
	learningRate = 0.1
	precision = 0.01
	if ('Hogwarts House' not in datas):
		return None
	nbr_subject = len(datas.columns) - 1
	nbr_house = datas['Hogwarts House'].nunique()
	thetas = [[0 for _ in range(nbr_subject)] for _ in range(nbr_house)]
	thetasNames = [["theta" + str(i) for i in range(nbr_subject)]]
	size = len(datas['Hogwarts House'].values)

	houseColumns = datas['Hogwarts House']
	houseNames = datas['Hogwarts House'].unique()
	print(houseNames)
	datas.drop('Hogwarts House', axis=1, inplace=True)
	subjectColumns = datas
	for iteration in range(30):
		tmpthetas = minimizeCostFunction(houseColumns, subjectColumns, thetas, learningRate, size, nbr_house, nbr_subject, houseNames)
	thetas = thetasNames + thetas	 
	return thetas

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

def main():
	vlen = len(sys.argv)
	if (vlen == 2):
		datas = csv.readCSVFile(sys.argv[1], ',')
		if (datas is None):
			sys.exit(1)
		subjectDatas = csv.dropColumns(datas, csv.ignoredSubjects)
		if (subjectDatas is None):
			sys.exit(1)
		datas = normalize(subjectDatas)
		thetas = train_prediction(datas.dropna().reset_index(drop=True))
		if (thetas == None):
			print("csv file incorect.")
			sys.exit(1)			
		csv.writeCSVFile('thetas.csv', thetas)
	else:
		print("Error script : python logreg_train.py file.")
if __name__ == "__main__":
	main()