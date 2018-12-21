#!~/.brew/bin/python
import csv
import pandas as pd
import numpy as np

# Global variables
houseNames = ['Slytherin', 'Hufflepuff', 'Gryffindor', 'Ravenclaw']
colors = ["#33c47f", "#A061D1", "#FF6950", "#4180db"]
notArithmetiqueSubjects = ['Index','First Name','Last Name','Birthday','Best Hand']
ignoredSubjects = nonArithmetiqueSubjects.append('Arithmancy', 'Defense Against the Dark Arts', 'Care of Magical Creatures', 'Transfiguration')

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

# Function dropColumns
# Params : (Dataframe) datas of the csv file ; list column to drop
# Return : return the same Dataframe but without the columns drop
def dropColumns(datas, columns):
	try:
		datas.drop(columns, axis=1, inplace=True)
	except Exception:
		print("One or multiple column beetween:", ", ".join(columns), "colum doesn't exits", sep=" ")
		return None
	return datas

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


# Function writeCSVFile
# Params : (String) fileName, [[name1, name2, ...], [value1, value2, ...], [value1, value2, ...], ...]
# Return : nothing
def writeCSVFile(fileName, datas):
	try:
		with open(fileName, mode='w+') as csv_file:
			fieldnames = datas[0]
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			writer.writeheader()
			dictionnary = {}
			for i in range(0, len(datas)):
				if (i != 0):
					dictionnary.update({fieldnames[i] : datas[i]})
			writer.writerow(dictionnary)
	except Exception:
		print 'The params must be a float[2].'
	except IOError:
		print 'The file thetas.csv isn\'t writable.'