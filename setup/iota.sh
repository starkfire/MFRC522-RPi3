#!/bin/bash

# https://medium.com/coinmonks/for-beginners-how-to-set-up-a-raspberry-pi-rfid-rc522-reader-and-record-data-on-iota-865f67843a2d

echo "[*] Installing foreign function interface library"
sudo apt-get install libffi-dev
echo "[*] Installing IOTA Distributed Ledger"
sudo pip install pyota[ccurl]
git clone https://github.com/iotaledger/iota.lib.py.git
cd iota.lib.py
python setup.py test
cd ..
