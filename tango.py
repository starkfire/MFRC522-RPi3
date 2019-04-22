# Tap-and-Go (Tango) Script
# automates the fare payment procedure

from cards import CardBalanceReducer, CardBalanceReader
from module.base import BaseCard
import base

import time
import csv
import pandas as pd
import numpy as np
import math

def check_card_present(obj):
	if obj.card is None:
		return false
	return True

# calculate distance with Haversine formula
# you can use Vincenty's formula, but I'm having issues with geopy recently
def haversine(pair1, pair2):
	R = 6372800
	lat1, lon1 = pair1
	lat2, lon2 = pair2
	phi1, phi2 = math.radians(lat1), math.radians(lat2)
	dphi = math.radians(lat2 - lat)
	dlambda = math.radians(lon2 - lon1)
	a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
	haversine_distance = 2*R*math.atan2(math.sqrt(a), math.sqrt(1-a))
	return haversine_distance

def last_known_location(log):
	tail_data = []
	with open(log, 'r') as loc:
		reader = csv.reader(loc, delimiter=',')
		for row in reader:
			if row:
				columns = [row[0], row[1]]
				tail_data.append(columns)
	last_row = tail_data[-1]
	lk_lat = last_row[0]
	lk_lon = last_row[1]
	return (lk_lat, lk_lon)

# needs further evaluation and a lot of refactoring
# i don't have device access now, so i might not be able to maintain this
# btw, had lots of issues
def main():
	# Log file references
	gpsl_log = 'logs/GPSLogger/gpslogger.csv'
	location_log = 'logs/location.csv'
	inbound_log = 'logs/inbound.csv'
	while True:
		outbound = None
		# snippet
		card = CardBalanceReader()
		if not check_card_present(card):
			print("Place card to reader")
		while not check_card_present(card):
			card.scan_card()
		# get UID
		UID = card.get_uid().get('uid')
		tail_uid = str(UID[0]) + str(UID[1]) + str(UID[2]) + str(UID[3]) + str(UID[4])
		# get last known location from location.csv
		init_lat, init_lon = last_known_location(location_log)
			
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		card = BaseCard()
		card.cleanup()
	card = BaseCard()
	card.cleanup()
