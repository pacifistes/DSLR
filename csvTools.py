#!~/.brew/bin/python
import csv
import pandas as pd
import numpy as np

# Global variables
houseNames = ['Slytherin', 'Hufflepuff', 'Gryffindor', 'Ravenclaw']
colors = ["#33c47f", "#A061D1", "#FF6950", "#4180db"]

# Function readCSVFile
# Params : (String) fileName of the csv file ; (Char) delimiter
# Return : reader object or None if error
def readCSVFile(fileName, delimiter):
	datas = None
	try:
		datas = pd.read_csv(fileName, delimiter)
	except IOError:
		print('The file doesn\'t exist or is not readable.')
	except Exception:
		print('Error in the file')
	return datas

# Function dropUselessColumn
# Params : (Dataframe) datas of the csv file ; (boolean) for dropHouseColumn
# Return : return the same Dataframe but without non numerical feature
def dropUselessColumn(datas, dropHouseColumn):
	subjectDatas = datas
	columnToDrop = ['Index','First Name','Last Name','Birthday','Best Hand']
	if (dropHouseColumn == True):
		columnToDrop.append('Hogwarts House')
	try:
		subjectDatas.drop(columnToDrop, axis=1, inplace=True)
	except Exception:
		print("One or multiple column beetween: Index,Hogwarts House,First Name,Last Name,Birthday,Best Hand colum doesn't exits")
		return None
	return subjectDatas

# Function dropNa 
# Params : List
# Return : return the list without nan value
def dropNa(datas):
	newDatas = []
	for data in datas:
		if (~np.isnan(data)):
			newDatas.append(data)
	return newDatas

# Function getSubjectValueByHouse
# Params : List
# Return : list of all Subject name and list of value by house by subject
# Exemple of return :[ [subject1, subject2,...], [ subject1[ House1[ note1, note2, ...], House2[ note1, note2, ...]], subject2[...], ...]]
def getSubjectValueByHouse(datas):
	subjectsByHouse = []
	subjectNames = []
	for data in datas:
		if (data == 'Hogwarts House'):
			continue
		subjectNames.append(data)
		tmpList = []
		for house in houseNames:
			tmpList.append(dropNa(datas[datas['Hogwarts House'].isin({house})][data].values))
		subjectsByHouse.append(tmpList)
	return [subjectNames, subjectsByHouse]
