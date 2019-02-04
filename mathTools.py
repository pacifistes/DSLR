#!~/.brew/bin/python
from __future__ import division
import numpy as np
import pandas as pd
import math



class Subject:

	def __init__(self, values):
		self.values = values

	def count(self):
		return np.count_nonzero(~pd.isnull(self.values))

	def mean(self):
		return np.nansum(self.values) / self.count()

	def std(self):
		vsum = 0
		meanValue = self.mean()
		for value in self.values:
			if (value == value):
				vsum += ((value - meanValue) ** 2) 
		result = sqrt((1 / self.count()) * vsum)
		return result

	def minimum(self):
		result = np.nan
		for value in self.values:
			if ((result != result and value == value) or (value == value and value < result)):
				result = value
		return result

	def maximum(self):
		result = np.nan
		for value in self.values:
			if ((result != result and value == value) or (value == value and value > result)):
				result = value
		return result

	def percentile(self, percentile):
		number = int(percentile * self.count())
		index = 0
		self.values.sort()
		for value in self.values:
			if (index == number):
				return value
			if (value == value):
				index += 1
		return 0

	def quart(self):
		return self.percentile(0.25)

	def half(self):
		return self.percentile(0.5)

	def threeQuarts(self):
		return self.percentile(0.75)

def sqrt(number):
	precision = 5
	value = 0
	while (value * value < number): 
		value += 1
	if (value * value == number):
		return number
	value -= 1
	increment = 0.1
	for i in range(0, precision):  
		while (value * value <= number): 
			value += increment
		value = value - increment 
		increment = increment / 10
	return value


def mean(values):
	return np.nansum(values) / count(values)


def count(values):
	return np.count_nonzero(~pd.isnull(values))