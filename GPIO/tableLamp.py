import RPi.GPIO as gp

LEDPin = 11
buttonPin = 12
LEDstate = False

def setup():
    gp.setmode(gp.BOARD)
    gp.setup(LEDPin, gp.OUT)
    gp.setup(buttonPin, gp.IN, pull_up_down = gp.PUD_UP)


def buttonEvent(channel):
    global LEDstate
    print(f'buttonEvent GPIO {channel}')
    LEDstate = not LEDstate
    if LEDstate:
        print('LED turned on')
    else:
        print('LED turned off')
    gp.output(LEDPin, LEDstate)

def loop():
    # button detect
    gp.add_event_detect(buttonPin, gp.FALLING, callback = buttonEvent,
                        bouncetime = 300)
    while True:
        pass

def finish():
    gp.cleanup()

if __name__ == '__main__':
    print('program is starting')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        finish()

