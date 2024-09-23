import RPi.GPIO as GPIO  # Import the GPIO library to control the Raspberry Pi's pins
import time  # Import the time library for delays

# Define pin numbers for each input and output
transmit_pin = 12  # Pin that receives the transmission signal
D_pin = 11  # Pin corresponding to D input on the wireless receiver
C_pin = 10  # Pin corresponding to C input on the wireless receiver
B_pin = 9  # Pin corresponding to B input on the wireless receiver
A_pin = 8  # Pin corresponding to A input on the wireless receiver
led_pin = 5  # Pin for the LED used for feedback

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)  # Use BCM numbering (refers to GPIO pin numbers)

# Set up output pins (for outputs that drive the tripod head)
GPIO.setup(0, GPIO.OUT)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

# Set up input pins (for receiving signals from the wireless controller)
GPIO.setup(A_pin, GPIO.IN)  # Pin A is set as an input pin
GPIO.setup(B_pin, GPIO.IN)  # Pin B is set as an input pin
GPIO.setup(C_pin, GPIO.IN)  # Pin C is set as an input pin
GPIO.setup(D_pin, GPIO.IN)  # Pin D is set as an input pin

# Set up the transmit pin and LED pin
GPIO.setup(transmit_pin, GPIO.IN)  # Pin to detect transmission signal
GPIO.setup(led_pin, GPIO.OUT)  # LED pin to give feedback on transmission

# The main loop that runs indefinitely
def loop():
    while True:
        # Check the status of the transmit pin
        transmit_signal = GPIO.input(transmit_pin)  # Read the state of the transmit pin

        if transmit_signal == 1:  # If the signal pin is HIGH (indicating a transmission)
            GPIO.output(led_pin, GPIO.HIGH)  # Turn on the LED for feedback

            # Iterate through all input pins (A, B, C, D) to check which is active
            for pin in [A_pin, B_pin, C_pin, D_pin]:  # Loop through the pins A to D
                if GPIO.input(pin):  # If the pin is HIGH (indicating a signal)
                    GPIO.output(pin - 8, GPIO.HIGH)  # Turn on the corresponding output pin
                    time.sleep(1)  # Wait for one second
                    GPIO.output(pin - 8, GPIO.LOW)  # Turn the output pin off

            GPIO.output(led_pin, GPIO.LOW)  # Turn off the LED after processing
            transmit_signal = 0  # Reset the transmit signal for the next loop

# Start the loop
if __name__ == "__main__":
    try:
        loop()  # Run the main loop
    except KeyboardInterrupt:
        GPIO.cleanup()  # Clean up the GPIO settings when the program is interrupted
