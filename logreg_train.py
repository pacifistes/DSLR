#!~/.brew/bin/python
import math as m
import sys
import csvTools as csv
import mathTools as math

# Function sigmoid
# Params : (Float) value
# Return : reader a value between 0 and 1
def	sigmoid(value):
	return 1 / (1 + m.e ** -value)

def costFunction(datas, thetas, house, m):
	cost = 0
	for line in range(datas.shape[0]):
		print(datas.iloc[[line]])
		# y = data[1]
		# xSigmoid = sigmoid(data[0] * theta)
		# cost = cost + (y * m.log10(xSigmoid) + (1 - y) * m.log10(1 - xSigmoid))
	return (-1 / m) * cost

def	minimizeCostFunction(datas, thetas, learningRate):
	for i, house in zip(range(datas['Hogwarts House'].nunique()), datas['Hogwarts House'].unique()):
		for subject, i_subject in zip(datas.columns, range(len(datas.columns) - 1)):
			if (subject == 'Hogwarts House'):
				continue
			m = math.count(datas[subject])
			thetas[i][i_subject] -= ((learningRate / m) * costFunction(datas,thetas[i], house, m))
	return thetas

def	train_prediction(datas):
	learningRate = 0.001
	precision = 0.000001
	if ('Hogwarts House' not in datas):
		return None
	thetas = [[0] * (len(datas.columns) - 1)] * datas['Hogwarts House'].nunique()
	thetasNames = [["theta" + str(i) for i in range(len(datas.columns))]]
	for iteration in range(0, 100):
		tmpthetas = minimizeCostFunction(datas, thetas, learningRate)
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
		thetas = train_prediction(subjectDatas)
		if (thetas == None):
			print("csv file incorect.")
			sys.exit(1)			
		csv.writeCSVFile('thetas.csv', thetas)
	else:
		print("Error script : python logreg_train.py file.")
if __name__ == "__main__":
	main()
