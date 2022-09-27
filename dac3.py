import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
nu=30
duty_cycle = int(input())
p = GPIO.PWM(22, nu)
p2 = GPIO.PWM(24, nu)
try:
    while True:
        if duty_cycle < 0 or duty_cycle > 100:
            raise ValueError("ot 0 do 100")
        p.start(duty_cycle)
        p2.start(duty_cycle)
finally:
    GPIO.output(22, 0)
    GPIO.output(24, 0)
    GPIO.cleanup()