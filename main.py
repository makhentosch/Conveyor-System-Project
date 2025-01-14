from webcam_qr_NO_GUI import *
from motor import *
import time

motor_running = False
motor1_forward(25)

def handle_qr_code(qr_data):

    global motor_running

    if motor_running:
        return

    if qr_data == "0":
        print("QR Code detected: Forward")
        motor2_forward(25)
        motor_running = True
        time.sleep(5)
        motor_running = False
        #qr_data = None
        motor2_stop()

    elif qr_data == "1":
        print("QR Code detected: Backward")
        motor2_backward(25)
        motor_running = True
        time.sleep(5)
        motor_running = False
        #qr_data = None
        motor2_stop()





try:
    while True:
    # Start scanning for QR codes and use the handle as a callback
        handle_qr_code(scan_qr_code())
        print("loop")
#    scanner.start_scanning(on_qr_detected=handle_qr_code)


except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting now...")

finally:
    # Release resources
    motor1_stop()
    motor2_stop()
    clean_pins()
    print("Resources released, program terminated")
