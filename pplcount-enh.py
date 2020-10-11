import RPi.GPIO as GPIO
import time

#GPIO mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO Pins
GPIO_TRIGGER = 17
GPIO_ECHO = 18

# IN / OUT of the pins
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set trigger auf HIGH
    GPIO.output(GPIO_TRIGGER, 1)

    # set trigger after 0.01ms on LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, 0)

    StartTsp = time.time()
    StopTsp = time.time()

    # StartTsp
    while GPIO.input(GPIO_ECHO) == 0:
        StartTsp = time.time()

    # Arrival of the wawe
    while GPIO.input(GPIO_ECHO) == 1:
        StopTsp = time.time()

    TimeElapsed = StopTsp - StartTsp
    # sound (34300 cm/s) 
    distance = (TimeElapsed * 34300) / 2

    return distance

def filterDiscance(distance):
    criticalRangeStart = 35
    criticalRangeEnd = 55

    if ( criticalRangeEnd > distance > criticalRangeStart):
        print ("person has passed at: %.1f" %distance)

    #print ("received destance is: %.1f" %distance)

if __name__ == '__main__':
    try:
        while True:
            filterDiscance(distance())
            time.sleep(1)

        # STRG+C reset
    except KeyboardInterrupt:
        print("mischief managed")
        GPIO.cleanup()