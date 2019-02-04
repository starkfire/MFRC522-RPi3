import RPi.GPIO as GPIO
import MFRC522
import signal
import sys


# All card objects inherint from this base class
class BaseCard(object):

    def __init__(self):
        self.MFReader = MFRC522.MFRC522()
        self.key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        signal.signal(signal.SIGINT, self.cleanup)
        self.authenticated = False
        self.card = None
        

    # A method to clean-up GPIO
    # once reading is finished
    def cleanup(self):
        "Ending reading..."
        "Cleaning GPIO"
        self.MFReader.MFRC522_StopCrypto1()
        GPIO.cleanup()

    # A method for scanning a card
    def scan_card(self):
        # print("Scanning for a card...")
        (status, TagType) = self.MFReader.MFRC522_Request(self.MFReader.PICC_REQIDL)
        if status == self.MFReader.MI_OK:
            print("Card detected")
            self.card = 1
            return True
        return None


    # A method for getting the UID of a card
    # Returns UID if grabbed else None
    def get_uid(self):
        (status, uid) = self.MFReader.MFRC522_Anticoll()
        if status == self.MFReader.MI_OK:
            print("Grabbed UID of card")
            self.uid = uid
            return {"uid": uid}
        return None

    # A method to authenticate
    # NOTE: must be called first before
    # Calling the methods below


    # TODO: Change this method to a decorator

    def authenticate(self):
        print("Authenticating")
        if not self.authenticated:
            self.MFReader.MFRC522_SelectTag(self.uid)
            status = self.MFReader.MFRC522_Auth(self.MFReader.PICC_AUTHENT1A, 8, self.key, self.uid)
            if status == self.MFReader.MI_OK:
                print("Authenticated")
                self.authenticated = True
                return
        return "Error! Already authenticated"


    # Sorry for the name
    # This function is called to get the desired data to write in the sector
    # Returns a list 
    def data_to_hexBits(self, amount):
        try:
            if self.check_for_negative(amount) and self.check_for_range(amount):
                new_data = self.data_to_list(amount)
                return new_data
        except:
            print("Error in parsing data")

    # This method is called to sanitize input against negative values
    def check_for_negative(self, amount):
        if not amount > 0:
            raise Exception("Amount should not be in negative value")
        return True


    # Checks if the input does not exceed 4080
    def check_for_range(self, amount):
        if amount > 4080:
            details = "Amount is beyond limit"
            raise Exception(details)
            return False
        return True


    # Convert the given amount to a list of numbers...
    # Example: 257 will be converted to [0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,2]
    def data_to_list(self, amount):
        extra = amount % 255
        counts = amount / 255
        new_data = []
        for i in range(counts):
            new_data.append(255)
        new_data.append(extra)

        range_ = len(new_data)
        for i in range(0, 16 - range_):
            new_data.insert(0, 0)

        return new_data
'''
        Data Representation
        each block is either 0 or 255
        Meaning, a block is either 0 or 1
        and we can compute 
          1      1      1    1      1    1      1    1      1    1      1    1      1    1      1    1 = 2^16 = 65536      
        [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,]
'''

class CardWriter(BaseCard):
    def __init__(self):
        super(CardWriter, self).__init__()

    # A method that writes data to a sector
    def write_sector(self, amount, sector=8):
        if not self.authenticated:
            self.authenticate()
        try:
            d = self.data_to_hexBits(amount)
            # print("Writing data {} to sector {}".format(d, sector))
            self.MFReader.MFRC522_Write(sector, d)
            block = self.read_sector(sector)['block']
            return {"block": block}
        except:
            return None

class CardReader(BaseCard):
    def __init__(self):
        super(CardReader, self).__init__()

    # A method to get a sector block
    # Takes in a number ranging 1 to 20

    def read_sector(self, sector=8):
        if not self.authenticated:
            self.authenticate()
        try:
            block = self.MFReader.MFRC522_Read(sector)
            return {
                "sector" : sector,
                "block" : block
                }
        except:
            return None

class CardWiper(BaseCard):
    def __init__(self):
        super(CardWiper, self).__init__()


    # A method for wiping sector 8 clean
    def clear_sector(self, sector=8):
        if not self.authenticated:
            self.authenticate()
        try:
            data = []
            for i in range(0, 16):
                data.append(0x00)
            # print("Clearing data for sector {}".format(sector))
            self.MFReader.MFRC522_Write(sector, data)
            block = self.read_sector(sector)['block']
            return {"block": block}
        except:
            return None


if __name__ == '__main__':
    pass
    '''
    data = reader.write_sector(sector=8, data=257)
    print(data)
    '''
    '''
    while not reader.get_uid():
        reader.get_uid()
    '''
