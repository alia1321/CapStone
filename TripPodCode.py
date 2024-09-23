import RPi.GPIO as GPIO
import time

# GPIO Pin assignments for controlling Bescor MP-101 movements
up_pin = 17       # GPIO pin connected to the "Up" control of Bescor MP-101
down_pin = 27     # GPIO pin connected to the "Down" control of Bescor MP-101
left_pin = 22     # GPIO pin connected to the "Left" control of Bescor MP-101
right_pin = 23    # GPIO pin connected to the "Right" control of Bescor MP-101
speed_pin = 18    # GPIO pin used for controlling the "Speed" with PWM

# Setup GPIO in BCM, Which means you gotta use the actual pin out of the raspberry pi and not the physical layout
GPIO.setmode(GPIO.BCM)

# Set the movement pins (Up, Down, Left, Right) as output pins
GPIO.setup([up_pin, down_pin, left_pin, right_pin], GPIO.OUT)

# Set up the speed pin as output for PWM (Pulse Width Modulation)
GPIO.setup(speed_pin, GPIO.OUT)

# Initialize PWM on the speed_pin with a frequency of 1 kHz
pwm = GPIO.PWM(speed_pin, 1000)  # 1000 Hz frequency
pwm.start(50)  # Start PWM with 50% duty cycle (medium speed)

# Function to move the tripod head up for a specified duration
def move_up(duration):
    GPIO.output(up_pin, GPIO.HIGH)  # Set "Up" pin to HIGH (turn on)
    time.sleep(duration)            # Keep moving up for the specified duration
    GPIO.output(up_pin, GPIO.LOW)   # Set "Up" pin to LOW (turn off)

# Function to move the tripod head down for a specified duration
def move_down(duration):
    GPIO.output(down_pin, GPIO.HIGH)  # Set "Down" pin to HIGH (turn on)
    time.sleep(duration)              # Keep moving down for the specified duration
    GPIO.output(down_pin, GPIO.LOW)   # Set "Down" pin to LOW (turn off)

# Function to move the tripod head left for a specified duration
def move_left(duration):
    GPIO.output(left_pin, GPIO.HIGH)  # Set "Left" pin to HIGH (turn on)
    time.sleep(duration)              # Keep moving left for the specified duration
    GPIO.output(left_pin, GPIO.LOW)   # Set "Left" pin to LOW (turn off)

# Function to move the tripod head right for a specified duration
def move_right(duration):
    GPIO.output(right_pin, GPIO.HIGH)  # Set "Right" pin to HIGH (turn on)
    time.sleep(duration)               # Keep moving right for the specified duration
    GPIO.output(right_pin, GPIO.LOW)   # Set "Right" pin to LOW (turn off)

# Function to adjust the speed by changing the PWM duty cycle
# The duty cycle is a percentage (0-100%) where a higher percentage means faster speed
def adjust_speed(duty_cycle):
    pwm.ChangeDutyCycle(duty_cycle)  # Change the speed by modifying the duty cycle

# Main program loop to demonstrate movement and speed control

# Main program loop, awaiting movement commands
try:
    # You can call movement functions like move_up(), move_down(), etc. with desired duration
    # For example:
    # move_up(2)  # Move up for 2 seconds
    # adjust_speed(75)  # Adjust speed to 75%

    pass  # Placeholder - no movement example, awaiting your commands

finally:
    # Clean up the GPIO pins to reset them when the program exits or is interrupted
    GPIO.cleanup()