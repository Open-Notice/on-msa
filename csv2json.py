import csv
import json

csvfile = open('ConsentMap2.csv', 'r')
jsonfile = open('consentmap3.json', 'w')

fieldnames = ("jurisdiction","legislation","legislationURL","policyReq","tosReq","purposeReq","contactReq","addressReq","dntReq")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
	json.dump(row, jsonfile)
	jsonfile.write('\n')
