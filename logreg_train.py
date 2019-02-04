#!~/.brew/bin/python
from logistic_regression import LogisticRegression
import sys

g_featureColumns =  ['Astronomy','Herbology','Defense Against the Dark Arts','Divination','Muggle Studies','Ancient Runes','History of Magic','Transfiguration','Potions','Charms','Flying']
# g_featureColumns =  ['Astronomy','Herbology','Divination','Muggle Studies','Ancient Runes','History of Magic']

def main():
	logistic = LogisticRegression('ressources/dataset_train.csv', 'Hogwarts House', g_featureColumns, 'ressources/dataset_test.csv')
	if (logistic.initTrain() is True):
		logistic.setLearningRate(2.8)
		logistic.setCostIteration(3)
		logistic.setNumberIteration(20)
		logistic.train()
		if (len(sys.argv) == 2 and sys.argv[1] == "-d"):
			print("preparation du display de la function cost")
			logistic.displayCost()

if __name__ == "__main__":
	main()