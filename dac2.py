import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setwarnings(False)


def decimal2binary(value):
    return[int(bit) for bit in bin(value)[2:].zfill(8)]

period = int(input("period: "))
try:
    while True:    
        for number in range(0, 255):
            number_bin = decimal2binary(number)
            time.sleep(period/512)
            for n, led in enumerate(dac):
                if number_bin[n] == 1:
                    GPIO.output(led, 1)
                else:
                    GPIO.output(led, 0)
        for number in range(255, 0, -1):
            number_bin = decimal2binary(number)
            time.sleep(period/512)
            for n, led in enumerate(dac):
                if number_bin[n] == 1:
                    GPIO.output(led, 1)
                else:
                    GPIO.output(led, 0)
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()