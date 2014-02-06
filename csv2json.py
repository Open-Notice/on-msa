import csv
import json

csvfile = open('ConsentMap.csv', 'r')
jsonfile = open('consentmap.json', 'w')

# create fieldnames corresponding to the column headers on the spreadsheet
fieldnames = ("jurisdiction","legislation","legislationURL","policyReq","tosReq","purposeReq","contactReq","addressReq","dntReq")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
	json.dump(row, jsonfile)
	jsonfile.write('\n')
