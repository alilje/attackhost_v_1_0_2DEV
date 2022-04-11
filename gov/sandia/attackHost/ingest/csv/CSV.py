import csv

with open('D:/tomichost-git/data/output/LOGS/2021.07.29.1701sysmon-data.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=':')
	line_count = 0
	for row in csv_reader:
		print(row)