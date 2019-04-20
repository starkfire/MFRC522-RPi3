# Tap-and-Go (Tango) Script
# automates the fare payment procedure

from cards import CardBalanceReducer
from module.base import BaseCard, CardWriter
import base

import numpy as np
import pandas as pd
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

def main():
	while True:
		card = CardBalanceReducer()
		if not check_card_present(card):
			print("Place card to reader")
		while not check_card_present(card):
			card.scan_card()
		# get UID
		UID = card.get_uid().get('uid')
		tail_uid = str(UID[0]) + str(UID[1]) + str(UID[2]) + str(UID[3]) + str(UID[4])
		# still have to add the other functions and stuff, I have to test them atm

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		card = BaseCard()
		card.cleanup()
	card = BaseCard()
	card.cleanup()
