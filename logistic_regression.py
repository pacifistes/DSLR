#!~/.brew/bin/python
from __future__ import division
from functools import partial
import math as m
import sys
import csvTools as csv
import mathTools as math
import pandas as pd
import numpy as np

class	LogisticRegression:
	def __init__(self, trainFilename, classifyColumn, featureColumns, predictFilename = None):
		self.trainFilename = trainFilename
		self.classifyColumn = classifyColumn
		self.featureColumns = list(featureColumns)
		self.predictFilename = predictFilename
		self.initTrainDone = False
		self.initPredictDone = False
		self.features = None
		self.predictFeatures = None
		self.classes = None
		self.thetas = None
		self.learningRate = 0.1
		self.numberIteration = 500
	
	def setLearningRate(self, learningRate):
		self.learningRate = learningRate
	
	def setNumberIteration(self, numberIteration):
		self.numberIteration = numberIteration

	def	predictAll(self):
		predicts = []
		if (self.initPredictDone is False):
			print("The function init must return True before call the function train")
			return None
		if (self.predictFilename is None):
			print("Add the predict filename in constructor")
			return None
		datas = csv.readCSVFile("thetas.csv" , ',')
		if (datas is None):
			return False
		# print(datas)
		try:
			thetas = datas[['theta0'] + self.featureColumns]
		except Exception:
			print("Error in thetas File")
			return None
		# print('**********')
		classNames = self.classes.unique()
		# print(classNames)
		# for lineThetas in thetas.values:
			# print(lineThetas)
		for values in self.predictFeatures.values:
			results = [self.predict(lineThetas, values.tolist()) for lineThetas in thetas.values]
			predicts.append(classNames[results.index(max(results)) - 1])
		
		dataframe = {}
		dataframe.update({self.classifyColumn : predicts})
		return pd.DataFrame(dataframe)

	def normalizePredictFile(self, trainFeatures, predictFeature):
		newFeatures = {}
		for feature in trainFeatures:
			values = trainFeatures[feature].values
			minimum = math.minimum(values)
			maximum = math.maximum(values)
			mean = (math.mean(values) - minimum) / (maximum - minimum)
			normalizeLambda = self.normalizeLambda(minimum, maximum)
			func = partial(self.applyNormalize ,mean, normalizeLambda)
			newFeatures.update({feature : map(func, predictFeature[feature].values)})
		newFeatures = pd.DataFrame(newFeatures)
		return newFeatures

	def initPredict(self):
		datas = csv.readCSVFile(self.trainFilename , ',')
		if (datas is None):
			return False
		try:
			trainFeatures = datas[self.featureColumns]
		except Exception:
			print("One or multiple columns beetween: ", ", ".join(self.featureColumns), " doesn't exits")
		try:
			self.classes = datas[self.classifyColumn]
		except Exception:
			print("the classify column ", self.classifyColumn, "doesn't exits")
		predictFeature = csv.readCSVFile(self.predictFilename , ',')
		if (predictFeature is None):
			return False
		try:
			predictFeature = predictFeature[self.featureColumns]
		except Exception:
			print("One or multiple columns beetween: ", ", ".join(self.featureColumns), " doesn't exits")
		self.predictFeatures = self.normalizePredictFile(trainFeatures, predictFeature)
		
		if (self.predictFeatures is not None):
			self.initPredictDone = True
		return self.initPredictDone

	# def getCost(self, classNames, iClass, line):
	# 	predict = self.predict(self.thetas[iClass], self.features.values[line].tolist())
	# 	result = m.log10(predict) if (self.classes[line] == classNames[iClass]) else m.log10(1 - predict)
	# 	return result * -1

	# def getFeatureTheta(self, classNames, iClass, iFeature):
	# 	getCost = partial(self.getCost, classNames, iClass)
	# 	cost = self.thetas[iClass][iFeature] + (math.mean(map(getCost, range(self.features.shape[0]))) * self.learningRate)
	# 	return theta

	def	sigmoid(self, value):
		return 1 / (1 + (m.e ** -value))

	def predict(self, thetas, values):
		values.insert(0, 1)		
		result = np.dot(thetas, values)
		return self.sigmoid(result)
	
	# def derivate(self, classNames, iClass, ifeature, line):
	# 	values = self.features.values[line].tolist()
	# 	values.insert(0, 1)
	# 	result = self.predict(self.thetas[iClass], values)
	# 	y = 1 if (self.classes[line] == classNames[iClass]) else 0
	# 	return (result - y) * values[ifeature]

	# def getFeatureTheta(self, classNames, iClass, iFeature):
	# 	derivate = partial(self.derivate, classNames, iClass, iFeature)
	# 	theta = self.thetas[iClass][iFeature] -  (self.learningRate * math.mean(map(derivate, range(self.features.shape[0]))))
	# 	return theta

	# def getClassThetas(self, classNames, iClass):
	# 	getFeatureTheta = partial(self.getFeatureTheta, classNames, iClass)
	# 	thetas = map(getFeatureTheta, range(self.features.shape[1] + 1))

	# 	return thetas

	# def	gradientDescent(self, classNames, iClasses):
	# 	getClassThetas = partial(self.getClassThetas, classNames)
	# 	self.thetas = map(getClassThetas, iClasses)

	def	gradientDescent2(self, classNames):
		self.thetas = [[self.thetas[iClass][iFeature] -  (self.learningRate * math.mean([(self.predict(self.thetas[iClass], values.tolist()) - 1 if (classtmp == className) else 0) * (1 if (iFeature == 0) else values[iFeature - 1])  for classtmp, values in zip(self.classes.values,self.features.values)])) \
		for iFeature in range(self.features.shape[1] + 1)] for iClass, className in enumerate(classNames)]

	def normalizeLambda(self, minimum, maximum):
		return lambda value : (value - minimum) / (maximum - minimum)

	def applyNormalize(self, mean, normalizeLambda, value):
		return mean if value != value else normalizeLambda(value)

	def normalize(self, features):
		newFeatures = {}
		for feature in features:
			values = features[feature].values
			minimum = math.minimum(values)
			maximum = math.maximum(values)
			mean = (math.mean(values) - minimum) / (maximum - minimum)
			normalizeLambda = self.normalizeLambda(minimum, maximum)
			func = partial(self.applyNormalize ,mean, normalizeLambda)
			newFeatures.update({feature : map(func, features[feature].values)})
		newFeatures = pd.DataFrame(newFeatures)
		return newFeatures

	def initTrain(self):
		datas = csv.readCSVFile(self.trainFilename , ',')
		if (datas is None):
			return False
		try:
			self.features = self.normalize(datas[self.featureColumns])
		except Exception:
			print("One or multiple columns beetween: ", ", ".join(self.featureColumns), " doesn't exits")
		try:
			self.classes = datas[self.classifyColumn]
		except Exception:
			print("the classify column ", self.classifyColumn, "doesn't exits")
		if (all(variable is not None for variable in [self.features, self.classes])):
			self.initTrainDone = True
		return self.initTrainDone
		
	# @profile
	def	train(self):
		if (self.initTrainDone is False):
			print("The function initTrain must return True before call the function train")
			return
		classNames = self.classes.unique()
		nbrClass = len(classNames)
		self.thetas = [[0.0 for _ in range(self.features.shape[1] + 1)] for _ in range(nbrClass)]
		for iteration in range(self.numberIteration):
			# self.gradientDescent(classNames, range(nbrClass))
			self.gradientDescent2(classNames)
		
		self.thetas = [["theta0"] + [feature for feature in self.featureColumns]] + self.thetas
		self.thetas[0].insert(0, self.classifyColumn)
		for className, iClass in zip(classNames, range(nbrClass)):
			self.thetas[iClass + 1].insert(0, className)
		self.thetas = np.asarray(self.thetas)
		self.thetas = pd.DataFrame(data=self.thetas[1:,0:], columns=self.thetas[0,0:])
		self.thetas.to_csv('thetas.csv', sep=',', index=False)