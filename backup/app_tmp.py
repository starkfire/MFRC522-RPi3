from cards import CardBalanceReader, CardBalanceAdder, CardBalanceReducer, CardBalanceWiper
from module.base import BaseCard
from module.wipe_card import main # since I don't have much time, I had to rush this... sorry
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
	elif choice == 4:
		print("Thank you! Good bye!")
        sys.exit()
        return

def main():
	welcome_message()
	print("Action: \n(1) Read current balance of card\n(2) Deposit to card\n(3) Pay using card\n(4) Exit")
	input_ = None
	while input_ is None or input_ not in [1,2,3, 4, 5]:
		try:
			choice = int(raw_input("Choose [1, 2, 3, or 4] "))
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
