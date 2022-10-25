import RPi.GPIO as GPIO
import time
from matplotlib import pyplot
GPIO.setmode(GPIO.BCM)
leds = [21, 20,16,12,7,8,25,24]
GPIO.setup(leds, GPIO.OUT)
dac = [26,19,13,6,5,11,9,10]
GPIO.setup(dac, GPIO.OUT, initial = GPIO.HIGH)
comp = 4
troyka = 17
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.output(leds, GPIO.LOW)

def adc():
    k = 0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(dac, dec2bin(k))
        time.sleep(0.005)
        if GPIO.input(comp) == 0:
            k-=2**i
    return k 

def dec2bin(value):
    return[int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    voltage = 0
    result = []
    time_start = time.time()
    count = 0
    GPIO.output(troyka, 1)
    print('nachalas zaryadka pozhilogo kondensatora')
    while voltage < 256*0.97:
        voltage = adc()
        result.append(voltage)
        print('zaryadka', (voltage/256)*3.3)
        count+=1
        GPIO.output(leds, dec2bin(voltage))
        
    GPIO.output(troyka, 0)
    
    print('nachalas razryadka pozhilogo kondensatora')
    while voltage > 256*0.02:
        voltage = adc()
        result.append(voltage)
        print('razryadka', (voltage/256)*3.3)
        count+=1
        GPIO.output(leds, dec2bin(voltage))

    time_now = time.time()
    time_of_experiment = time_now - time_start

    print('konec experimenta')

    with open('data.txt', 'w') as f:
        for res in result:
            f.write(str(res) + '\n')
    f.close()
    with open('settings.txt', 'w') as f:
        f.write(str(count/time_of_experiment) + '\n')
        f.write('0.013')
    print(count, count/time_of_experiment)
    f.close()
    y = [res/256*3.3 for res in result]
    x = [i*time_of_experiment/count for i in range(len(result))]
    pyplot.plot(x, y)
    pyplot.show()

finally:
    GPIO.output(leds, GPIO.LOW)
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()