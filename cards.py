from module.base import CardReader, CardWriter, CardWiper, BaseCard, CardWiper
import RPi.GPIO as GPIO
import MFRC522
import signal
import sys

class CardBalanceReader(CardReader):
	def __init__(self):
		super(CardBalanceReader, self).__init__()

	def get_card(self):
		print("Please place card to reader")
		while self.card is None:
			self.scan_card()
			uid = self.get_uid()
		return uid or None

	def get_current_balance(self):
		amount = 0
		if self.card is None:
			self.get_card()
		block = self.read_sector()
		block = block.get('block')
		for i in reversed(block):
			if i == 0:
				break
			else:
				amount += i
		print("Current Balance: {}".format(amount))
		return amount


class CardBalanceAdder(CardWriter, CardBalanceReader):
	def __init__(self):
		super(CardBalanceAdder, self).__init__()


	def get_deposit(self):
		while True:
			try:
				deposit = int(raw_input("Input your desired deposit... "))
				break
			except ValueError:
				raise Except("Deposit must be a whole number, not in decimal or letters")
		return deposit or None

	def add_balance(self, deposit=None):
		while deposit is None or deposit == 0:
			deposit = self.get_deposit()
		amount = 0
		if self.card is None:
			self.get_card()
		block = self.read_sector()
		block = block.get('block')
		for i in reversed(block):
			if i == 0:
				break
			else:
				amount += i
		new_amount = amount + deposit
		self.write_sector(amount=new_amount)
		print("New Balance: {}".format(new_amount))
		return new_amount

class CardBalanceReducer(CardWriter, CardBalanceReader):
	def __init__(self):
		super(CardBalanceReducer, self).__init__()

	def check_card_present(obj):
		if obj.card is None:
			return False
		return True

	def scan_card(self):
        # print("Scanning for a card...")
        (status, TagType) = self.MFReader.MFRC522_Request(self.MFReader.PICC_REQIDL)
        if status == self.MFReader.MI_OK:
            print("Card detected")
            self.card = 1
            return True
        return None

	def get_uid(self):
        (status, uid) = self.MFReader.MFRC522_Anticoll()
        if status == self.MFReader.MI_OK:
            self.uid = uid
            return {"uid": uid}
        return None

	#def get_custom_fee(self):
	#	while True:
	#		try:
	#			fee = int(raw_input("Input your desired fee ..."))
	#			break
	#		except ValueError:
	#			raise Except("Fee must be in whole number")
	#	return fee or None

	# Reduce current amount
	def reduce_balance(self, fee=None):
		while fee is None or fee == 0:
			fee = self.get_custom_fee()
		current_balance = self.get_current_balance()
		if current_balance < fee:
			print("Ooops! Insufficient balance!")
			return
		new_balance = current_balance - fee
		self.write_sector(amount=new_balance)
		print("New Balance: {}".format(new_balance))
		time.sleep(3)
		return new_balance


class CardBalanceWiper(CardWiper, CardBalanceReader):
	def __init__(self):
		super(CardBalanceWiper, self).__init__()
