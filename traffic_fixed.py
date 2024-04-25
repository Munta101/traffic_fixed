from machine import Pin
import utime

# Define pin numbers for each traffic light signal
RED1_PIN = 32
YELLOW1_PIN = 33
GREEN1_PIN = 25

RED2_PIN = 27
YELLOW2_PIN = 14
GREEN2_PIN = 12

RED3_PIN = 23
YELLOW3_PIN = 22
GREEN3_PIN = 21

RED4_PIN = 16
YELLOW4_PIN = 17
GREEN4_PIN = 5

# Initialize the pin objects for each traffic light signal
red1 = Pin(RED1_PIN, Pin.OUT)
yellow1 = Pin(YELLOW1_PIN, Pin.OUT)
green1 = Pin(GREEN1_PIN, Pin.OUT)

red2 = Pin(RED2_PIN, Pin.OUT)
yellow2 = Pin(YELLOW2_PIN, Pin.OUT)
green2 = Pin(GREEN2_PIN, Pin.OUT)

red3 = Pin(RED3_PIN, Pin.OUT)
yellow3 = Pin(YELLOW3_PIN, Pin.OUT)
green3 = Pin(GREEN3_PIN, Pin.OUT)

red4 = Pin(RED4_PIN, Pin.OUT)
yellow4 = Pin(YELLOW4_PIN, Pin.OUT)
green4 = Pin(GREEN4_PIN, Pin.OUT)


# Function to control the traffic light signals
def control_traffic_lights():
    # Set initial state
    red1.value(1)
    yellow1.value(0)
    green1.value(0)

    red2.value(1)
    yellow2.value(0)
    green2.value(0)

    red3.value(1)
    yellow3.value(0)
    green3.value(0)

    red4.value(1)
    yellow4.value(0)
    green4.value(0)

    while True:
        # Intersection 1: Green light
        green1.value(1)
        red2.value(1)
        utime.sleep(10)  # Green light duration
        green1.value(0)
        yellow1.value(1)
        utime.sleep(2)  # Yellow light duration
        yellow1.value(0)
        red1.value(1)
        yellow2.value(0)
        green2.value(1)
        utime.sleep(1)  # Delay between changing lights

        # Intersection 2: Green light
        green2.value(1)
        red1.value(1)
        utime.sleep(10)  # Green light duration
        green2.value(0)
        yellow2.value(1)
        utime.sleep(2)  # Yellow light duration
        yellow2.value(0)
        red2.value(1)
        yellow3.value(0)
        green3.value(1)
        utime.sleep(1)  # Delay between changing lights

        # Intersection 3: Green light
        green3.value(1)
        red2.value(1)
        utime.sleep(10)  # Green light duration
        green3.value(0)
        yellow3.value(1)
        utime.sleep(2)  # Yellow light duration
        yellow3.value(0)
        red3.value(1)
        yellow4.value(0)
        green4.value(1)
        utime.sleep(1)  # Delay between changing lights

        # Intersection 4: Green light
        green4.value(1)
        red3.value(1)
        utime.sleep(10)  # Green light duration
        green4.value(0)
        yellow4.value(1)
        utime.sleep(2)  # Yellow light duration
        yellow4.value(0)
        red4.value(1)
        yellow1.value(0)
        green1.value(1)
        utime.sleep(1)  # Delay between changing lights


# Start controlling the traffic lights
control_traffic_lights()
