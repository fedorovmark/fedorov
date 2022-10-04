import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
led = [24, 25, 8, 7, 12, 16, 20, 21]
troykaModule = 17
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
comp = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def decimal2binary(value):
    return[int(bit) for bit in bin(value)[2:].zfill(8)]
def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal
try:
    sig = [0, 0 , 0 , 0 , 0 , 0 , 0 , 0]
    while True:
        for value in range(256):
            time.sleep(0.001)
            signal = num2dac(value)
            voltage = value/levels * maxVoltage
            compar_val = GPIO.input(comp)
            if compar_val == 0:
                percentage = voltage/maxVoltage
                GPIO.output(led, sig)
                if percentage>0 and percentage<=0.125:
                    sig = [0, 0 , 0 , 0 , 0 , 0 , 0 , 0]
                elif percentage>0.125 and percentage<=0.25:
                    sig = [0, 0 , 0 , 0 , 0 , 0 , 0 , 1]
                elif percentage>0.25 and percentage<=0.375:
                    sig = [0, 0 , 0 , 0 , 0 , 0, 1 , 1]
                elif percentage>0.375 and percentage<=0.5:
                    sig = [0, 0 , 0 , 0 , 0 , 1 , 1 , 1]
                elif percentage>0.5 and percentage<=0.625:
                    sig = [0, 0 , 0 , 0, 1 , 1 , 1 , 1]    
                elif percentage>0.625 and percentage<=0.75:
                    sig = [0, 0 , 0, 1 , 1 , 1 , 1 , 1]
                elif percentage>0.75 and percentage<=0.875:
                    sig = [0, 0, 1 , 1 , 1 , 1 , 1 , 1]
                elif percentage>0.875 and percentage<1:
                    sig = [0, 1 , 1 , 1 , 1 , 1 , 1 , 1]
                elif percentage == 1:
                    sig = [1, 1 , 1 , 1 , 1 , 1 , 1 , 1]
                print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))
                break
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
