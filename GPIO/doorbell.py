import RPi.GPIO as gpio

buzzerPin = 11
buttonPin = 12

def setup():
    gpio.setmode(gpio.BOARD)
    gpio.setup(buzzerPin, gpio.OUT)
    gpio.setup(buttonPin, gpio.IN, pull_up_down = gpio.PUD_UP)

def loop():
    while True:
        if gpio.input(buttonPin) == False:
            gpio.output(buzzerPin, True)
            print('buzzer turned on')
        else:
            gpio.output(buzzerPin, False)
            print('buzzer turned OFF')

def finish():
    gpio.cleanup()


if __name__ == '__main__':
    print('program is starting')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        finish()
