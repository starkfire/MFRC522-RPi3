import csv
import pandas as pd
import numpy as np

#ds_raw = 'logs/gpslogger.csv'
ds_raw = 'gpslogger.csv'
ds_read = pd.read_csv(ds_raw, delimiter=',', names=['time','lat','lon'])
