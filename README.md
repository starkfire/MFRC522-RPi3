Jeep-Beeper
===========
Originally a fork of the [jeep-beeper](https://github.com/dertrockx/jeep-beeper) repo, this project attempts to implement a contactless payment system for Public Utility Vehicles (e.g. Jeepneys). 

While emulating the beep Card used in the LRT/MRT system, this attempt is station-independent, where the transportation fees depend on the distance traversed by the vehicle during a passenger's stay inside the vehicle instead of relying on fixed stations. 

This variant uses an Android phone for geolocation and currently uses the GPSLogger app for fetching geodata, which will be used for calculating the transportation fee.

## Requirements
* This code requires the SPI-Py installed. Get it from the [offical github repo](https://github.com/lthiery/SPI-Py)
* Also, I used [this module](https://github.com/mxgxw/MFRC522-python)

## Pins

| Name | Pin # | Pin name   |
|:------:|:-------:|:------------:|
| SDA  | 24    | GPIO8      |
| SCK  | 23    | GPIO11     |
| MOSI | 19    | GPIO10     |
| MISO | 21    | GPIO9      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO25     |
| 3.3V | 1     | 3V3        |

## Usage
1. Install SPI-Py from [here](https://github.com/lthiery/SPI-Py)
2. Run ``` python app.py ```

## Experimental Variants
Two variants will be implemented with this project. These variants will implement distance-dependent fare rate using GPS data from an Android phone. Vincenty's Formulae will be used for approximating the P2P distance.

1. GPSL+ Variant
* a variant that will use the GPSLogger app for dynamic fare charges by retrieving location data using an Android phone

2. FCPClient Variant
* similar to GPSL+. However, unlike GPSL+, this variant will use the [Fused Location Provider API](https://developers.google.com/location-context/fused-location-provider/) for fetching location data and implement a TCP socket for retrieving data
