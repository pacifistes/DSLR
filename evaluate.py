from __future__ import division
# import numpy as np
import pandas as pd


if __name__ == '__main__':
	# Load the truths
	truths = pd.read_csv('ressources/dataset_truth.csv', sep=',', index_col=0)
	# Load predictions
	predictions = pd.read_csv('ressources/houses.csv', sep=',', index_col=0)
	# Replace names by numerical value {0, 1, 2, 3} and convert to array
	houses = {'Gryffindor': 0, 'Hufflepuff': 1, 'Ravenclaw': 2, 'Slytherin': 3}
	realValue = truths.replace(houses).values
	predict = predictions.replace(houses).values
	totalTrue = 0
	
	totalTrueTable = [0 for _ in range(4)]
	totalPredictTable = [0 for _ in range(4)]
	totalEachHouse = [0 for _ in range(4)]

	for true, predict in zip(realValue, predict):
		if (true[0] == predict[0]):
			totalPredictTable[predict[0]] += 1
			totalTrue += 1
		totalTrueTable[true[0]] += 1
		totalEachHouse[predict[0]] += 1
	print('prediction :' + str(totalTrue / len(realValue)))
	print('\nGrynfondor :' + str(totalPredictTable[0]) + "/" + str(totalTrueTable[0]))
	print('Hufflepuff :' + str(totalPredictTable[1]) + "/" + str(totalTrueTable[1]))
	print('Ravenclaw :' + str(totalPredictTable[2]) + "/" + str(totalTrueTable[2]))
	print('Slytherin :' + str(totalPredictTable[3]) + "/" + str(totalTrueTable[3]))
	print('\nGrynfondor :' + str(totalEachHouse[0]))
	print('Hufflepuff :' + str(totalEachHouse[1]))
	print('Ravenclaw :' + str(totalEachHouse[2]))
	print('Slytherin :' + str(totalEachHouse[3]))