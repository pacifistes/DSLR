#!~/.brew/bin/python
import math

# Function sigmoid
# Params : (Float) value
# Return : reader a value between 0 and 1
def	sigmoid(value):
	return 1 / (1 + math.e ** -value)

def costFunction(datas):
	cost = 0
	m = len(datas)
	for data in datas:
		y = data[1]
		xSigmoid = sigmoid(data[0])
		cost = cost + (y * math.log10(xSigmoid) + (1 - y) * math.log10(1 - xSigmoid))
	return (-1 / m) * cost

def	minimizeCostFunction(datas, theta):
	learningRate = 0.001
	m = len(datas)
	cost = 0

	for data in datas:
		x = data[0]
		y = data[1]
		cost = cost + ((sigmoid(x) - y) * x)
	return theta - ((learningRate / m) * cost)

def	findTheta(datas):
	theta = 0.0
	thetaPres = 0.000001
	for iteration in range(0,100000000):
		tmpTheta = minimizeCostFunction(datas, theta)
		if (abs(theta - tmpTheta) < thetaPres):
			break
		theta = tmpTheta
	return theta