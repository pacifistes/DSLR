#!~/.brew/bin/python
from logistic_regression import LogisticRegression

g_featureColumns = ['Astronomy','Herbology','Divination','Muggle Studies','Ancient Runes','History of Magic']

def main():
	logistic = LogisticRegression('ressources/dataset_train.csv', 'Hogwarts House', g_featureColumns, 'ressources/dataset_test.csv')
	if (logistic.initTrain() is True):
		logistic.train()

if __name__ == "__main__":
	main()