#!~/.brew/bin/python
from logistic_regression import LogisticRegression
import sys

g_featureColumns = ['Astronomy','Herbology','Divination','Muggle Studies','Ancient Runes','History of Magic']

def main():
	logistic = LogisticRegression('ressources/dataset_train.csv', 'Hogwarts House', g_featureColumns, 'ressources/dataset_test.csv')
	# logistic = LogisticRegression('ressources/data_plop.csv', 'Passed', g_plop, 'ressources/dataset_test.csv')
	if (logistic.initTrain() is True):
		logistic.setLearningRate(0.1)
		logistic.setCostIteration(50)
		logistic.setNumberIteration(500)
		logistic.train()
		if (len(sys.argv) == 2 and sys.argv[1] == "-displayCost"):
			print("preparation du display de la function cost")
			logistic.displayCost()

if __name__ == "__main__":
	main()