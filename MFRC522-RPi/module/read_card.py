import base

if __name__ == '__main__':
	reader = base.CardReader()
	reader.scan_card()
	reader.get_uid()
	print("Read what block?")
	while True:
		try:
			sector = int(input())
			break
		except TypeError:
			print("Input a number")

	block = reader.read_sector(sector=sector)
	print(block)
