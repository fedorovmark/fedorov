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

def bin2dec(signal):
    return sum([signal[i-1] * 2**(bits-i) for i in range(1, bits+1)])
try:
    sig = [0, 0 , 0 , 0 , 0 , 0 , 0 , 0]
    while True:
        signal  = [0]*bits
        for i in range(bits):
            signal[i] = 1
            GPIO.output(dac, signal)
            time.sleep(0.1)
            comp_val = GPIO.input(comp)
            if comp_val == 0:
                signal[i] = 0
        
        value = bin2dec(signal)
        voltage = value/levels * maxVoltage
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
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
