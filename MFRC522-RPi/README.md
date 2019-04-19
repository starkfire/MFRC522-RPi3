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
