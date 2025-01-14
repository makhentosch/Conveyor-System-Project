import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)
MOT1_1 = 2  # GPIO pin connected to IN1 on the motor driver
MOT1_2 = 3  # GPIO pin connected to IN2 on the motor driver
MOT1_3 = 5  
MOT1_4 = 6 
GPIO.setup(MOT1_1, GPIO.OUT)
GPIO.setup(MOT1_2, GPIO.OUT)
GPIO.setup(MOT1_3, GPIO.OUT)
GPIO.setup(MOT1_4, GPIO.OUT)
PWMmot1_1 = GPIO.PWM(MOT1_1, 100)
PWMmot1_2 = GPIO.PWM(MOT1_2, 100)
PWMmot1_3 = GPIO.PWM(MOT1_3, 100)
PWMmot1_4 = GPIO.PWM(MOT1_4, 100)


MOT2_1 = 23
MOT2_2 = 24
MOT2_3 = 8
MOT2_4 = 7
GPIO.setup(MOT2_1, GPIO.OUT)
GPIO.setup(MOT2_2, GPIO.OUT)
GPIO.setup(MOT2_3, GPIO.OUT)
GPIO.setup(MOT2_4, GPIO.OUT)
PWMmot2_1 = GPIO.PWM(MOT2_1, 100)
PWMmot2_2 = GPIO.PWM(MOT2_2, 100)
PWMmot2_3 = GPIO.PWM(MOT2_3, 100)
PWMmot2_4 = GPIO.PWM(MOT2_4, 100)

PWMmot1_1.start(0)
PWMmot1_2.start(0)
PWMmot1_3.start(0)
PWMmot1_4.start(0)

PWMmot2_1.start(0)
PWMmot2_2.start(0)
PWMmot2_3.start(0)
PWMmot2_4.start(0)


def motor1_forward(speed):
        PWMmot1_1.ChangeDutyCycle(speed)
        PWMmot1_2.ChangeDutyCycle(0)
        PWMmot1_3.ChangeDutyCycle(speed)
        PWMmot1_4.ChangeDutyCycle(0)


#    GPIO.output(IN1, GPIO.HIGH)
#    GPIO.output(IN2, GPIO.LOW)

def motor2_forward(speed):
        PWMmot2_1.ChangeDutyCycle(speed)
        PWMmot2_2.ChangeDutyCycle(0)
        PWMmot2_3.ChangeDutyCycle(speed)
        PWMmot2_4.ChangeDutyCycle(0)        

def motor2_backward(speed):
        PWMmot2_1.ChangeDutyCycle(0)
        PWMmot2_2.ChangeDutyCycle(speed)
        PWMmot2_3.ChangeDutyCycle(0)
        PWMmot2_4.ChangeDutyCycle(speed)
#    GPIO.output(IN1, GPIO.LOW)
#    GPIO.output(IN2, GPIO.HIGH)

def motor2_stop():
        PWMmot2_1.ChangeDutyCycle(0)
        PWMmot2_2.ChangeDutyCycle(0)
        PWMmot2_3.ChangeDutyCycle(0)
        PWMmot2_4.ChangeDutyCycle(0)

def motor1_stop():
        PWMmot1_1.ChangeDutyCycle(0)
        PWMmot1_2.ChangeDutyCycle(0)
        PWMmot1_3.ChangeDutyCycle(0)
        PWMmot1_4.ChangeDutyCycle(0)

def clean_pins():
        PWMmot1_1.stop(0)
        PWMmot1_2.stop(0)
        PWMmot1_3.stop(0)
        PWMmot1_4.stop(0)

        PWMmot2_1.stop(0)
        PWMmot2_2.stop(0)
        PWMmot2_3.stop(0)
        PWMmot2_4.stop(0)
        GPIO.cleanup()

#    GPIO.output(IN1, GPIO.LOW)
#    GPIO.output(IN2, GPIO.LOW)

#motor1_forward(25)
#motor2_forward(25)
#time.sleep(7)

#motor2_backward(30)
#time.sleep(7)
#motor_stop()

# Cleanup


