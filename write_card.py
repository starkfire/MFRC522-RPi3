import base



# Checks if card is already scanned by checking the 'card' property
# The writer instance is passed to this function as 'obj'
def check_card_present(obj):
	if obj.card is None:
		return False
	return True

# The writer instance is passed to this function as 'obj'
def write_data_to_card(obj, amount=None):
	if amount is None:
		try:
			amount = int(input("Input amount "))
		except:
			print("Please input a number")
			write_data_to_card(obj, amount)
	block = obj.write_sector(amount=amount)
	return block


def main():
	card = base.CardWriter()
	print("Scanning card ...")
	if not check_card_present(card):
		print("Please place card to reader")
	while not check_card_present(card):
		card.scan_card()
	UID = card.get_uid().get('uid')
	print("UID of card: {}-{}-{}-{}-{}".format(UID[0], UID[1], UID[2], UID[3], UID[4]))
	write_data_to_card(card)




if __name__ == '__main__':
	main()