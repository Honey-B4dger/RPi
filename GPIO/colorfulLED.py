import RPi.GPIO as gpio
import time
import random

pins = {'pinRed': 11, 'pinGreen': 12, 'pinBlue': 13}

def setup():
    global pwmRed, pwmGreen, pwmBlue
    gpio.setmode(gpio.BOARD)
    for key, pin in pins.items():
        gpio.setup(pin, gpio.OUT)
        gpio.output(pin, True)
    #gpio.setup(pins, gpio.OUT)
    #gpio.output(pins, True)

    pwmRed = gpio.PWM(pins['pinRed'], 2000)
    pwmGreen = gpio.PWM(pins['pinGreen'], 2000)
    pwmBlue = gpio.PWM(pins['pinBlue'], 2000)

    pwmRed.start(0)
    pwmGreen.start(0)
    pwmBlue.start(0)

def setColor(r_val, g_val, b_val):
    pwmRed.ChangeDutyCycle(r_val)
    pwmGreen.ChangeDutyCycle(g_val)
    pwmBlue.ChangeDutyCycle(b_val)

def loop():
    while True:
        r = random.randint(0,100)
        g = random.randint(0,100)
        b = random.randint(0,100)

        setColor(r,g,b)
        print(f'r: {r}, g: {g}, b: {b}')
        time.sleep(1)

def finish():
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    gpio.cleanup()


if __name__ == '__main__':
    print('Program starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        finish()
