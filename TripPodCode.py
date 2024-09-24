import RPi.GPIO as GPIO
import time

# GPIO Pin assignments for controlling Bescor MP-101 movements
UP_PIN = 17       # GPIO pin connected to the "Up" control of Bescor MP-101
DOWN_PIN = 27     # GPIO pin connected to the "Down" control of Bescor MP-101
LEFT_PIN = 22     # GPIO pin connected to the "Left" control of Bescor MP-101
RIGHT_PIN = 23    # GPIO pin connected to the "Right" control of Bescor MP-101
# SPEED_PIN = 18    # GPIO pin used for controlling the "Speed" with PWM (if applicable)

# Setup GPIO in BCM (Broadcom SOC channel) mode
GPIO.setmode(GPIO.BCM)

# Set the movement pins (Up, Down, Left, Right) as output pins with initial LOW state
GPIO.setup(UP_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DOWN_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LEFT_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RIGHT_PIN, GPIO.OUT, initial=GPIO.LOW)

# Commented out speed control until confirmed it's supported
GPIO.setup(SPEED_PIN, GPIO.OUT)
 pwm = GPIO.PWM(SPEED_PIN, 1000)  # 1000 Hz frequency
 pwm.start(50)  # Start PWM with 50% duty cycle (medium speed)

# Function to move the tripod head up for a specified duration
def move_up(duration):
    GPIO.output(UP_PIN, GPIO.HIGH)  # Activate "Up" movement
    time.sleep(duration)
    GPIO.output(UP_PIN, GPIO.LOW)   # Deactivate "Up" movement

# Function to move the tripod head down for a specified duration
def move_down(duration):
    GPIO.output(DOWN_PIN, GPIO.HIGH)  # Activate "Down" movement
    time.sleep(duration)
    GPIO.output(DOWN_PIN, GPIO.LOW)   # Deactivate "Down" movement

# Function to move the tripod head left for a specified duration
def move_left(duration):
    GPIO.output(LEFT_PIN, GPIO.HIGH)  # Activate "Left" movement
    time.sleep(duration)
    GPIO.output(LEFT_PIN, GPIO.LOW)   # Deactivate "Left" movement

# Function to move the tripod head right for a specified duration
def move_right(duration):
    GPIO.output(RIGHT_PIN, GPIO.HIGH)  # Activate "Right" movement
    time.sleep(duration)
    GPIO.output(RIGHT_PIN, GPIO.LOW)   # Deactivate "Right" movement

# Function to adjust the speed by changing the PWM duty cycle (if applicable)
# def adjust_speed(duty_cycle):
#     pwm.ChangeDutyCycle(duty_cycle)  # Change the speed by modifying the duty cycle

# Main program loop to demonstrate movement
try:
    # Example movements
    print("Moving up for 2 seconds")
    move_up(2)
    
    print("Moving down for 2 seconds")
    move_down(2)
    
    print("Moving left for 2 seconds")
    move_left(2)
    
    print("Moving right for 2 seconds")
    move_right(2)
    
    # Adjust speed if supported
    # print("Adjusting speed to 75%")
    # adjust_speed(75)

except KeyboardInterrupt:
    print("Program interrupted by user.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up the GPIO pins to reset them when the program exits or is interrupted
    GPIO.cleanup()
    print("GPIO cleanup completed.")
