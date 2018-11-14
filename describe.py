#!~/.brew/bin/python
import tools
import sys
import pandas as pd
import numpy as np

def main():
	if len(sys.argv) == 2:
		# datas = tools.readCSVFile(sys.argv[1], ',')
		# for data in datas:
			# print data
		df = pd.read_csv(sys.argv[1], sep=',')
		listt = df.describe()
		# df = pd.DataFrame({'$a':['a', 'b', 'c', 'd', 'a'], '$b': np.arange(5)})
		# listt = df.describe(include = 'all')
		print listt
	else:
		print 'Error script : python describe.py file.'


if __name__ == "__main__":
	main()
