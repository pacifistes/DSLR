#!~/.brew/bin/python
from __future__ import division
from functools import partial
import multiprocessing
import concurrent.futures
import math as m
import sys
import csvTools as csv
import mathTools as math
import pandas as pd
import numpy as np

g_featureColumns = ['Astronomy','Herbology','Divination','Muggle Studies','Ancient Runes','History of Magic']

class	LogisticRegression:
	def __init__(self, trainFilename, classifyColumn, featureColumns):
		self.trainFilename = trainFilename
		self.classifyColumn = classifyColumn
		self.featureColumns = list(featureColumns)
		self.features = None
		self.classes = None
		self.thetas = None
		self.__learningRate = 0.1
		self.__numberIteration = 3
		self.__isInitDoneSuccessfully = False
	
	def __normalizeLambda(self, minimum, maximum):
		return lambda value : (value - minimum) / (maximum - minimum)

	def __applyNormalize(self, mean, normalizeLambda, value):
		return mean if value != value else normalizeLambda(value)

	def __normalize(self, features):
		newFeatures = {}
		for feature in features:
			values = features[feature].values
			minimum = math.minimum(values)
			maximum = math.maximum(values)
			mean = (math.mean(values) - minimum) / (maximum - minimum)
			normalizeLambda = self.__normalizeLambda(minimum, maximum)
			func = partial(self.__applyNormalize ,mean, normalizeLambda)
			newFeatures.update({feature : map(func, features[feature].values)})
		newFeatures = pd.DataFrame(newFeatures)
		return newFeatures

	def	__sigmoid(self, value):
		return 1 / (1 + (m.e ** -value))

	def __predict(self, thetas, values):
		result = 0.0
		for i in range(len(thetas)):
			result += (thetas[i] * values[i])
		return self.__sigmoid(result)

	def __getCost(self, line)
		y = 0 + (self.classes[line] == className)
		predict = self.__predict(self.thetas[iClass], self.features[iFeature][line])
		return 

	def __getFeatureTheta()
		theta = self.thetas[][] - ((sum(map(self.__getCost, self.features.shape[0])) \
		* (-1 / self.features.shape[0])) * (self.__learningRate / self.features.shape[0]))
		return theta

	def __getClassThetas(self, className):
		getFeatureThetas = partial(self.__getFeatureThetas, className)
		return map(getFeatureThetas, self.features)

	def	__minimizeCostFunction(self, classNames, nbrClass, nbrFeature, nbrLine):
		self.thetas = map(self.getClassThetas, classNames)

	# def	__minimizeCostFunction(self, classNames, nbrClass, nbrFeature, nbrLine):
	# 	# return None
	# 	for iClass, className in zip(range(nbrClass), classNames):
	# 		for iFeature in range(nbrFeature):
	# 			cost = 0
	# 			for line in range(nbrLine):
	# 				y = 0 + (self.classes[line] == className)
	# 				predict = self.__predict(self.thetas[iClass], self.features[iFeature][line])
	# 				cost = cost + (y * m.log10(predict) + (1 - y) * m.log10(1 - predict))
	# 			self.thetas[iClass][iFeature] -= ((self.__learningRate / nbrLine) * ((-1 / nbrLine) * cost))

	def setLearningRate(self, learningRate):
		self.__learningRate = learningRate
	
	def setNumberIteration(self, numberIteration):
		self.__numberIteration = numberIteration

	@profile
	def init(self):
		datas = csv.readCSVFile(self.trainFilename , ',')
		if (datas is None):
			return False
		try:
			self.features = self.__normalize(datas[self.featureColumns])
		except Exception:
			print("One or multiple columns beetween: ", ", ".join(self.featureColumns), " doesn't exits")
		try:
			self.classes = datas[self.classifyColumn]
		except Exception:
			print("the classify column ", self.classifyColumn, "doesn't exits")
		if (all(variable is not None for variable in [self.features, self.classes])):
			self.__isInitDoneSuccessfully = True
			return True
		return False

	def	train(self):
		if (self.__isInitDoneSuccessfully is False):
			print("The function init must return True before call the function train")
			return False
		nbrFeature = len(self.features.shape[1])
		classNames = self.classes.unique()
		nbrClass = len(classNames)
		nbrLine = self.feature.shape[0]
		self.thetas = [[0.0 for _ in range(nbrFeature)] for _ in range(nbrClass)]
		for iteration in range(self.__numberIteration):
			self.__minimizeCostFunction(classNames, nbrClass, nbrFeature, nbrLine)
		self.thetas = [[feature for feature in self.featureColumns]] + self.thetas
		return True
		

# @profile
def main():
	vlen = len(sys.argv)
	if (vlen == 2):
		logistic = LogisticRegression('ressources/dataset_train.csv', 'Hogwarts House', g_featureColumns)
		if (logistic.init()):
			logistic.train()
			# logistic.writeThetas
		# datas = csv.readCSVFile(sys.argv[1], ',')
		# if (datas is None):
		# 	sys.exit(1)
		# subjectDatas = csv.dropColumns(datas, csv.ignoredSubjects)
		# if (subjectDatas is None):
		# 	sys.exit(1)
		# datas = normalize(subjectDatas)
		# sys.exit(1)
		# thetas = train_prediction(datas)
		# if (thetas == None):
		# 	print("csv file incorect.")
		# 	sys.exit(1)			
		# csv.writeCSVFile('thetas.csv', thetas)
	else:
		print("Error script : python logreg_train.py file.")

if __name__ == "__main__":
	main()



# def normalize6(L, values , nbr_line):
# 		minimum = math.maximum(values)
# 		maximum = math.minimum(values)
# 		mean = (math.mean(values) - minimum) / (maximum - minimum)
# 		my = mylambda(minimum, maximum)
# 		L.append(getValue3(mean, my, values[line]) \
# 		for line in range(nbr_line))

# def testManager(subjectDatas):
# 	with multiprocessing.Manager() as manager:
# 		L = manager.list()  # <-- can be shared between processes.
# 		processes = []
# 		for subject in subjectDatas:
# 			p = multiprocessing.Process(target=normalize6, args=(L,subjectDatas[subject], subjectDatas.shape[0]))  # Passing the list
# 			p.start()
# 			processes.append(p)
# 		for p in processes:
# 			p.join()
# 	return L

# def testPool2(subjectDatas):
# 	num_processes = multiprocessing.cpu_count()
# 	with concurrent.futures.ProcessPoolExecutor(num_processes) as pool:
# 		result = []
# 		for subject in subjectDatas:
# 			values = subjectDatas[subject].values
# 			minimum = math.maximum(values)
# 			maximum = math.minimum(values)
# 			mean = (math.mean(values) - minimum) / (maximum - minimum)
# 			func = partial(getValue2,mean, minimum, maximum)
# 			result.append(list(pool.map(func, values)))
# 			break
# 		return result

# def testPool3(subjectDatas):
# 	num_processes = multiprocessing.cpu_count()
# 	with concurrent.futures.ProcessPoolExecutor(num_processes) as pool:
# 		result = []
# 		for subject in subjectDatas:
# 			values = subjectDatas[subject].values
# 			minimum = math.maximum(values)
# 			maximum = math.minimum(values)
# 			mean = (math.mean(values) - minimum) / (maximum - minimum)
# 			my = mylambda(minimum, maximum)
# 			func = partial(getValue3,mean, my)
# 			result.append(list(pool.map(func, values)))
# 		return result