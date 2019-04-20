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
