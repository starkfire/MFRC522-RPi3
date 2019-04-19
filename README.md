Jeep-Beeper
===========
A simple script that utilizes the Raspberry Pi and a MFRC522 module to emulate the beep payment system of LRT / MRT for jeepneys.


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
