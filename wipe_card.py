import base

def check_card_present(obj):
	if obj.card is None:
		return False
	return True

def handle_choice(card, choice='y'):
	unsafe_choices = ['y', 'yes']
	if choice.lower() in unsafe_choices:
		print("Scanning card ...")
		if not check_card_present(card):
			print("Please place card to reader")
		while not check_card_present(card):
			card.scan_card()
		card.get_uid()
		card.clear_sector()
		return {"detail": "Successful in wiping card"}
	return {"detail": "Error in wiping card"}

def main():
	card = base.BaseCard()
	print("Wiping card clean...")
	choice = str(raw_input("Confirm? [y/N]"))
	detail = handle_choice(card, choice=choice)
	print(detail['detail'])

if __name__ == '__main__':
	main()
