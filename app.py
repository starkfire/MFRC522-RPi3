from cards import CardBalanceReader, CardBalanceAdder, CardBalanceReducer
from module.base import BaseCard
import sys


def welcome_message():
	print("Welcome!! \t Beep Card for Jeepney")

def handle_choice(choice):
	if choice == 1:
		card = CardBalanceReader()		
		return card.get_current_balance()
	elif choice == 2:
		card = CardBalanceAdder()
		return card.add_balance()
	elif choice == 3:
		card = CardBalanceReducer()
		return card.reduce_balance()
	else:
		return None


def main():
	welcome_message()
	print("Action: \n1. Read current balance of card\n2. Deposit to card\n3. Pay using card")
	input_ = None
	while input_ is None or input_ not in [1,2,3]:
		try:
			choice = int(raw_input("Choice [1, 2, or 3] "))
			input_ = choice
		except ValueError:
			print("Please input a number, not a character or text")

	obj = handle_choice(choice=input_)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		card = BaseCard
		card.cleanup()
	card = BaseCard()
	card.cleanup()

