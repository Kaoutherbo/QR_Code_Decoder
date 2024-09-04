# QR-Code-Decoder

A Python script that decodes QR codes containing Wi-Fi credentials and extracts the SSID, encryption type, and password. I initially built this just for fun to get the Wi-Fi password of my neighbor (don't worry, I didn't use it yet! 😜, but i will 😁💀). It's a handy tool for decoding Wi-Fi QR codes from images and getting the password quickly.

## Features
- Decode Wi-Fi QR codes (SSID, encryption type, password, hidden status).
- Extract and print Wi-Fi password directly from the QR code.

## Requirements

Make sure you have Python 3.x installed on your machine. You'll also need the following Python libraries:

- `opencv-python`
- `pyzbar`

You can install them using pip:

```bash
pip install opencv-python pyzbar
```
## Usage
- Clone the repository:
```bash
git clone https://github.com/yourusername/WiFi-QR-Decoder.git
cd WiFi-QR-Decoder
```
Place the QR code image file in the same directory, or specify its path in the script.

- Run the Python script:

```bash
python main.py
```
- Example output:
```bash
Decoded QR Data: WIFI:S:MyNetwork;T:WPA;P:password123;H:false;;
Wi-Fi Password: password123
```
## Code Explanation
- The script reads the QR code image using OpenCV and decodes it using the pyzbar library.
- It extracts the Wi-Fi SSID, encryption type, and password from the QR code data and prints the password.
