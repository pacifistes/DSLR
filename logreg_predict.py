#!~/.brew/bin/python
from logistic_regression import LogisticRegression
from logreg_train import g_featureColumns

def main():
	logistic = LogisticRegression('ressources/dataset_train.csv', 'Hogwarts House', g_featureColumns, 'ressources/dataset_test.csv')
	if (logistic.initPredict()):
			result = logistic.predictAll()
			if (result is not None):
				result.to_csv('ressources/houses.csv', sep=',', index=True, index_label='Index')

if __name__ == "__main__":
	main()

