import pandas as pd
import numpy as np
import csv

# CSV file containing the filtered output
post_log = 'logs/location.csv'
# CSV File containing the original output from GPSLogger
ds_import = 'logs/gpslogger.csv'

tail_data = []
with open(ds_import, 'r') as ds:
    reader = csv.reader(ds, delimiter=',')
    for row in reader:
        if row:
            columns = [row[1], row[2]]
            tail_data.append(columns)

last_row = tail_data[-1]
new_row = [last_row[0], last_row[1]]
with open(post_log, 'a') as loc:
    log_in = csv.writer(loc)
    log_in.writerow(new_row)
loc.close()
