import time
import RPi.GPIO as GPIO

# Set up the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Get user input for the countdown duration
countdown_time = int(input("Enter the number of seconds for the countdown: "))

# Perform the countdown
for i in range(countdown_time, 0, -1):
    print(i)
    time.sleep(1)

# Turn on the LED for 3 seconds
GPIO.output(18, GPIO.HIGH)
time.sleep(3)
GPIO.output(18, GPIO.LOW)

# Text alert
print("Time's up!")

# Clean up the GPIO settings
GPIO.cleanup()

