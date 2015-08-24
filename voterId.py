### Author: Michael Hugman
### A script to retrieve voter ID from a csv file, given a first and last name


import csv
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#query = input("Enter the voter's name: ")
query_L = "LOGAN"
query_F = "SUSAN"
query_M = ""

choices = []


with open('test.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		rowText = ', '.join(row)
		
		lastName = re.findall(r'^(?:[^,]*,){5}(.*?),.*$', rowText)[0]
		lastName = lastName.replace('"','')

		ratio = fuzz.ratio(query, lastName)

		if ratio > 50: 
			voterId = re.findall(r'^.*?"(.*?)".*$', rowText)[0]
			choices.append((lastName, voterId))

		print ratio
		print "\n"

print choices
		