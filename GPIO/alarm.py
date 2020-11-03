import RPi.GPIO as gpio
import time
import math

buzzerPin = 11
buttonPin = 12

def setup():
    global p
    gpio.setmode(gpio.BOARD)
    gpio.setup(buzzerPin, gpio.OUT)
    gpio.setup(buttonPin, gpio.IN, pull_up_down = gpio.PUD_UP)

    p = gpio.PWM(buzzerPin, 1)
    p.start(0)

def loop():
    while True:
        if gpio.input(buttonPin) == False:
            alarm()
            #print('alarm turned on')
        else:
            stopAlarm()
            #print('alarm turned OFF')


def alarm():
    p.start(50)
    for x in range(0, 361):
        sinVal = math.sin(x * (math.pi / 180))
        toneVal = 1001 + sinVal * 1000
        p.ChangeFrequency(toneVal)
        time.sleep(0.01)

def stopAlarm():
    p.stop()

def finish():
    gpio.output(buzzerPin, False)
    gpio.cleanup()


if __name__ == '__main__':
    print('program is starting')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        finish()
