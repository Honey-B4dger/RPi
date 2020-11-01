import RPi.GPIO as GPIO
import time

ledPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    print(f'Using {ledPin}')

def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        print('LED turned on >>>')
        time.sleep(0.1)
        GPIO.output(ledPin, GPIO.LOW)
        print('LED turned off <<<')
        time.sleep(0.1)

def finish():
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        finish()
