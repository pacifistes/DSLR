#!~/.brew/bin/python
from __future__ import division
import numpy as np
import math

def count(values):
	return np.count_nonzero(~np.isnan(values))

def mean(values):
	return np.nansum(values) / count(values)

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

def std(values):
	vsum = 0
	meanValue = mean(values)
	for value in values:
		if (value == value):
			vsum += ((value - meanValue) ** 2) 
	result = sqrt((1 / count(values)) * vsum)
	return result


def minimum(values):
	result = np.nan
	for value in values:
		if ((result != result and value == value) or (value == value and value < result)):
			result = value
	return result

def maximum(values):
	result = np.nan
	for value in values:
		if ((result != result and value == value) or (value == value and value > result)):
			result = value
	return result

def percentile(values, percentile):
	number = int(percentile * count(values))
	index = 0
	values.sort()
	for value in values:
		if (index == number):
			return value
		if (value == value):
			index += 1
	return 0

def quart(values):
	return percentile(values, 0.25)

def half(values):
	return percentile(values, 0.5)

def threeQuarts(values):
	return percentile(values, 0.75)