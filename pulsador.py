from EmulatorGUI import GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
GPIO.setup(7, GPIO.OUT)

while True:
    if GPIO.input(3):
        GPIO.output(7,GPIO.LOW)
    else:
        GPIO.output(7,GPIO.HIGH)

