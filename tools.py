#!~/.brew/bin/python
import csv
import pandas as pd
import numpy as np

# Function readCSVFile
# Params : (String) fileName of the csv file ; (Char) delimiter
# Return : reader object or None if error
def readCSVFile(fileName, delimiter):
	datas = None
	try:
		datas = pd.read_csv(fileName, delimiter)
		# print datas.describe()
	except IOError:
		print 'The file doesn\'t exist or is not readable.'
	except Exception:
		print 'Error in the file'
	return datas

# Function getSubjectDatas
# Params : (Dataframe) datas of the csv file
# Return : return the same Dataframe but without non numerical feature
def getSubjectDatas(datas):
	subjectDatas = datas
	try:
		subjectDatas.drop(['Index','Hogwarts House','First Name','Last Name','Birthday','Best Hand'], axis=1, inplace=True)
	except Exception:
		print "One or multiple column beetween: Index,Hogwarts House,First Name,Last Name,Birthday,Best Hand colum doesn't exits"
		return None
	return subjectDatas

def getSubjectDatasWithHouse(datas):
	subjectDatas = datas
	try:
		subjectDatas.drop(['Index','First Name','Last Name','Birthday','Best Hand'], axis=1, inplace=True)
	except Exception:
		print "One or multiple column beetween: Index,Hogwarts House,First Name,Last Name,Birthday,Best Hand colum doesn't exits"
		return None
	return subjectDatas

def dropNa(datas):
	newDatas = []
	for data in datas:
		if (~np.isnan(data)):
			newDatas.append(data)
	return newDatas

def getSubjectValueByHouse(datas) :
	subjectsByHouse = []
	subjectNames = []
	houseNames = ['Slytherin', 'Hufflepuff', 'Gryffindor', 'Ravenclaw']
	colors = ["#33c47f", "#A061D1", "#FF6950", "#4180db"]

	for data in datas:
		if (data == 'Hogwarts House'):
			continue
		subjectNames.append(data)
		tmpList = []
		# i = 0
		for house in houseNames:
			tmpList.append(dropNa(datas[datas['Hogwarts House'].isin({house})][data].values))
			# if (i == 0):
				# print datas[datas['Hogwarts House'].isin({house})][data].values
			# i += 1
		subjectsByHouse.append(tmpList)
	return [subjectNames, subjectsByHouse, houseNames, colors]

def sqrt(value):
	return 1