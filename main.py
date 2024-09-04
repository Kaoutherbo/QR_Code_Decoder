import cv2
from pyzbar.pyzbar import decode

def extract_wifi_password(decoded_data):
    parts = decoded_data.split(';')
    for part in parts:
        if part.startswith('P:'):
            return part[2:]
    return None

def decode_qr_code(image_path):
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Error: Unable to load image from {image_path}. Check the path.")
        return None

    qr_codes = decode(img)

    if len(qr_codes) == 0:
        print("No QR code detected in the image.")
        return None

    for qr_code in qr_codes:
        qr_data = qr_code.data.decode('utf-8')
        return qr_data

image_path = 'wifi_qrcode.png'
decoded_data = decode_qr_code(image_path)

if decoded_data:
    print(f"Decoded QR Data: {decoded_data}")
    password = extract_wifi_password(decoded_data)
    if password:
        print(f"Wi-Fi Password: {password}")
    else:
        print("No password found in the QR code.")
