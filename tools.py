#!~/.brew/bin/python
import csv

# Function readCSVFile
# Params : (String) fileName of the csv file ; (Char) delimiter
# Return : reader object or None if error
def readCSVFile(fileName, delimiter):
	datas = None
	try:
		f = open(fileName, mode='r')
		try:
			datas = csv.reader(f, delimiter=delimiter)
			next(datas)
		except Exception:
			print 'Error in the file'
	except IOError:
		print 'The file thetas.csv doesn\'t exist or is not readable.'
	return datas