from __future__ import division
import numpy as np
import pandas as pd


if __name__ == '__main__':
	# Load the truths
	truths = pd.read_csv('ressources/dataset_truth.csv', sep=',', index_col=0)
	# Load predictions
	predictions = pd.read_csv('ressources/houses.csv', sep=',', index_col=0)
	# Replace names by numerical value {0, 1, 2, 3} and convert to array
	houses = {'Gryffindor': 0, 'Hufflepuff': 1, 'Ravenclaw': 2, 'Slytherin': 3}
	y_true = truths.replace(houses).values
	y_pred = predictions.replace(houses).values
	print(len(y_true))
	print(len(y_pred))
	totalTrue = 0
	for true, predict in zip(y_true, y_pred):
		if (true == predict):
			totalTrue += 1
	print('prediction :' + str(totalTrue / len(y_true)))