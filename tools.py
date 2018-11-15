#!~/.brew/bin/python
import csv
import pandas as pd

# Function readCSVFile
# Params : (String) fileName of the csv file ; (Char) delimiter
# Return : reader object or None if error
def readCSVFile(fileName, delimiter):
	datas = None
	try:
		datas = pd.read_csv(fileName, delimiter)
		print datas.describe()
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
