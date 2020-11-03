import RPi.GPIO as gpio
import time

LEDPin = 12

def setup():
    global p
    gpio.setmode(gpio.BOARD)
    gpio.setup(LEDPin, gpio.OUT)
    gpio.output(LEDPin, False)

    p = gpio.PWM(LEDPin, 500)
    p.start(0)

def loop():
    while True:
        for dc in range(0,101,1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.005)
        time.sleep(0)
        for dc in range(100,-1,-1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.005)
        time.sleep(0)

def finish():
    gpio.cleanup()


if __name__ == '__main__':
    print('Program starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        finish()
