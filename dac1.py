import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setwarnings(False)
def func(a):
    return[int(i) for i in bin(a)[2:].zfill(8)]

try:
    while True:
        a = input()
        if(a.isdigit()):
            a = int(a)
            if 0<=a<=255:
                GPIO.output(dac, func(a))
                print("{:.3f}".format(3.3/256*a))
            elif a<0 or a>255:
                raise ValueError("a<256 and a>=0")
        else:
            if a=='q':
                break
            raise ValueError("only numbers")
finally:
    GPIO.output(dac, 1)
    GPIO.cleanup()