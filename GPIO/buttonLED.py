import RPi.GPIO as GPIO

ledPin = 11
buttonPin = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            GPIO.output(ledPin, GPIO.HIGH)
            #print('LED turned on')
        else:
            GPIO.output(ledPin, GPIO.LOW)
            #print('LED turned off')

def finish():
    GPIO.cleanup()


if __name__ == '__main__':
    print('Program starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        finish()
