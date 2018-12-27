#!~/.brew/bin/python
from __future__ import division
from functools import partial
import math as m
import sys
import csvTools as csv
import mathTools as math
import pandas as pd
import numpy as np

g_featureColumns = ['Astronomy','Herbology','Divination','Muggle Studies','Ancient Runes','History of Magic']

class	LogisticRegression:
	def __init__(self, trainFilename, classifyColumn, featureColumns, predictFilename=None):
		self.trainFilename = trainFilename
		self.predictFilename = predicFilename
		self.classifyColumn = classifyColumn
		self.featureColumns = list(featureColumns)
		self.features = None
		self.predicFeatures = None
		self.classes = None
		self.thetas = None
		self.__minimums = None
		self.__maximums = None
		self.__means = None
		self.__learningRate = 0.3
		self.__numberIteration = 250
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
			self.__minimums.append(minimum)
			self.__maximums.append(maximum)
			self.__means.append(mean)
			func = partial(self.__applyNormalize ,mean, normalizeLambda)
			newFeatures.update({feature : map(func, features[feature].values)})
		newFeatures = pd.DataFrame(newFeatures)
		return newFeatures

	def __normalizePredictFile(self, features):
		newFeatures = {}
		for feature, iFeature in zip(features, range(features.shape[1])):
			values = features[feature].values
			minimum = self.__minimum[iFeature]
			maximum = self.__maximum[iFeature]
			mean = self.__mean[iFeature]
			normalizeLambda = self.__normalizeLambda(minimum, maximum)
			func = partial(self.__applyNormalize ,mean, normalizeLambda)
			newFeatures.update({feature : map(func, features[feature].values)})
		newFeatures = pd.DataFrame(newFeatures)
		return newFeatures

	def	__sigmoid(self, value):
		return 1 / (1 + (m.e ** -value))

	def __predict(self, thetas, values):
		values.insert(0, 1)
		result = np.dot(thetas, values)
		return self.__sigmoid(result)
	
	def __derivate(self, classNames, iClass, ifeature, line):
		values = self.features.values[line].tolist()
		result = self.__predict(self.thetas[iClass], values)
		y = 1 if (self.classes[line] == classNames[iClass]) else 0
		return (result - y) * values[ifeature]

	# def __getCost(self, classNames, iClass, line):
	# 	predict = self.__predict(self.thetas[iClass], self.features.values[line].tolist())
	# 	result = m.log10(predict) if (self.classes[line] == classNames[iClass]) else m.log10(1 - predict)
	# 	return result * -1

	# def __getFeatureTheta(self, classNames, iClass, iFeature):
	# 	getCost = partial(self.__getCost, classNames, iClass)
	# 	cost = self.thetas[iClass][iFeature] + (math.mean(map(getCost, range(self.features.shape[0]))) * self.__learningRate)
	# 	return theta

	def __getFeatureTheta(self, classNames, iClass, iFeature):
		derivate = partial(self.__derivate, classNames, iClass, iFeature)
		theta = self.thetas[iClass][iFeature] -  (self.__learningRate * math.mean(map(derivate, range(self.features.shape[0]))))
		return theta

	def __getClassThetas(self, classNames, iClass):
		getFeatureTheta = partial(self.__getFeatureTheta, classNames, iClass)
		thetas = map(getFeatureTheta, range(self.features.shape[1] + 1))
		return thetas

	def	__gradientDescent(self, classNames, iClasses):
		getClassThetas = partial(self.__getClassThetas, classNames)
		self.thetas = map(getClassThetas, iClasses)

	def setLearningRate(self, learningRate):
		self.__learningRate = learningRate
	
	def setNumberIteration(self, numberIteration):
		self.__numberIteration = numberIteration

	def init(self):
		datas = csv.readCSVFile(self.trainFilename , ',')
		if (datas is None):
			return False
		try:
			self.features = self.__normalize(datas[self.featureColumns])
			if (self.predictFilename != None):
				datas = csv.readCSVFile(self.predicFilename , ',')
				if (datas is None):
					return False
				self.predicFeatures = self.__normalizePredictFile(datas[self.featureColumns])
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
		classNames = self.classes.unique()
		nbrClass = len(classNames)
		self.thetas = [[0.0 for _ in range(self.features.shape[1] + 1)] for _ in range(nbrClass)]
		for iteration in range(self.__numberIteration):
			self.__gradientDescent(classNames, range(nbrClass))
		self.thetas = [["theta0"] + [feature for feature in self.featureColumns]] + self.thetas
		self.thetas[0].insert(0, self.classifyColumn)
		for className, iClass in zip(classNames, range(nbrClass)):
			self.thetas[iClass + 1].insert(0, className)
		return True

	def	predictAll(self):
		predicts = []
		if (self.__isInitDoneSuccessfully is False):
			print("The function init must return True before call the function train")
			return None
		if (self.predictFilename is None):
			print("Add the predict filename in constructor")
			return None
		datas = csv.readCSVFile(self.predicFilename , ',')
		if (datas is None):
			return False
		thetas = datas['thetas0' + self.featureColumns]
		print(thetas)

	def writeThetas(self):
		if (self.__isInitDoneSuccessfully is False):
			print("The function init must return True before call the function train")
			return
		csv.writeCSVFile('thetas.csv', self.thetas)


def main():
	vlen = len(sys.argv)
	if (vlen == 2):
		logistic = LogisticRegression('ressources/dataset_train.csv', 'Hogwarts House', g_featureColumns)
		if (logistic.init() and logistic.train()):
			logistic.writeThetas()
	else:
		print("Error script : python logreg_train.py file.")

if __name__ == "__main__":
	main()