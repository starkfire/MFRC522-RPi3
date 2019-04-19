# MFRC522-RPi3 (GPSL+)

### Overview
* This variant (GPSL+) uses the GPSLogger app for fetching location data using an Android phone

### Contents
This contains scripts for
* parsing CSV files sent by the GPSLogger app to the Raspberry Pi via FTP and extract location data
* using Vincenty's formulae for approximating distance between the start and end point of travel
* dynamically adjusting the fare rate charge for BalanceReducer() based on P2P distance calculation
