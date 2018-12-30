#!~/.brew/bin/python
from logistic_regression import LogisticRegression

g_featureColumns = ['Astronomy','Herbology','Divination','Muggle Studies','Ancient Runes','History of Magic']

def main():
	logistic = LogisticRegression('ressources/dataset_train.csv', 'Hogwarts House', g_featureColumns, 'ressources/dataset_test.csv')
	if (logistic.initPredict()):
			result = logistic.predictAll()
			if (result is not None):
				result.to_csv('ressources/houses.csv', sep=',', index=True, index_label='Index')

if __name__ == "__main__":
	main()

