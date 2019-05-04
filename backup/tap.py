from cards import CardBalanceReducer
import base
from module.base import BaseCard, CardWriter
from module.wipe_card import main

import pandas as pd
import numpy as np
import math

def check_card_present(obj):
    if obj.card is None:
        return false
    return True

def haversine(pair1, pair2):
    R = 6372800
    lat1, lon1 = pair1
    lat2, lon2 = pair2
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1-a))

def last_known_location(ds_import):
    tail_data = []
    with open()
    lklat = np.genfromtxt(location_log, delimiter=',', names=['lat'])
    lk_latitude = lklat[-1:]
    lklon = np.genfromtxt(location_log, delimiter=',', names=['lon'])
    lk_longitude = lklon[-1:]
    return (lk_latitude, lk_longitude)

def main():
    gpsl_log = 'logs/gpslogger.csv'
    location_log = 'logs/location.csv'
    inbound_log = 'logs/inbound.csv'
    while True:
        card = CardBalanceReducer()
        if not check_card_present(card):
            print("Place card to reader")
        while not check_card_present(card):
            card.scan_card()
        # get UID of card
        UID = card.get_uid().get('uid')
        tail_uid = str(UID[0])+str(UID[1])+str(UID[2])+str(UID[3])+str(UID[4])
        # fetch last known location
        initial_pair = last_known_location(location_log)
        # determine if an inbound or outbound passenger
        io_uid = pd.read_csv(inbound_log, delimiter=',', names=['uid'])
        for row in io_read:
            for field in row:
                if field == io_uid:
                    io_read = pd.read_csv(inbound_log, delimiter=',')
                    match = io_read[io_read.source == io_uid]
                    get_flat = list(match.lat)
                    get_flon = list(match.lon)
                    final_pair = get_flat, get_flon
                    computed_fare = haversine(initial_pair, final_pair)
                    card.reduce_balance(fee=computed_fare)
                else:
                    # bind UID with the last known location
                    newline = [tail_lat, tail_lon, tail_uid]
                    # write data to log
                    with open(inbound_log, 'a') as inbound:
                        log_in = csv.writer(inbound)
                        log_in.writerow(newline)
                    inbound.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        card = BaseCard()
        card.cleanup()
    card = BaseCard()
    card.cleanup()
