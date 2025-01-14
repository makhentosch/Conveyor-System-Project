
import cv2
from pyzbar.pyzbar import decode
import time

def scan_qr_code():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture image")
            break

        # Decode QR codes in the frame
        decoded_objects = decode(frame)
        for barcode in decoded_objects:
            # Decode and print the QR code data
            qr_data = barcode.data.decode('utf-8')
            print("QR Code Data:", qr_data)
            return qr_data

    # Release the webcam
    cap.release()
