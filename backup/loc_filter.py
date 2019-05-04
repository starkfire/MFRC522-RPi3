# Script for filtering data from GPSLogger

import csv
import time

# GPSLogger log file
ds_import = 'logs/GPSLogger/gpslogger.csv'
# filtered locations log
post_log = 'logs/location.csv'

while True:
	tail_data = []
	with open(ds_import, 'r') as ds:
		reader = csv.reader(ds, delimiter=',')
		for row in reader:
			if row:
				columns = [row[1], row[2]]	# lat and lon
				tail_data.append(columns)
	last_row = tail_data[-1]
	new_row = [last_row[0], last_row[1]]
	with open(post_log, 'a') as loc:
		log = csv.writer(loc)
		log.writerow(new_row)
	loc.close()
	print(new_row)
	time.sleep(5)		# fetch every 5 seconds
