from tkinter import *
import RPi.GPIO as GPIO
import time

# setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Define GPIO pins
W_CLK = 3
FQ_UD = 5
DATA = 7
RESET = 11

# setup IO bits
GPIO.setup(W_CLK, GPIO.OUT)
GPIO.setup(FQ_UD, GPIO.OUT)
GPIO.setup(DATA, GPIO.OUT)
GPIO.setup(RESET, GPIO.OUT)

# initialize everything to zero
GPIO.output(W_CLK, False)
GPIO.output(FQ_UD, False)
GPIO.output(DATA, False)
GPIO.output(RESET, False)

# Function to send a pulse to GPIO pin
def pulseHigh(pin):
    GPIO.output(pin, True)
    GPIO.output(pin, True)
    GPIO.output(pin, False)
    return

# Function to send a byte to AD9850 module
def tfr_byte(data):
    for i in range (0,8):
        GPIO.output(DATA, data & 0x01)
        pulseHigh(W_CLK)
        data=data>>1
    return
# Function to send frequency (assumes 125MHz xtal) to AD9850 module
def sendFrequency(frequency):
    freq=int(frequency*4294967296/125000000)
    for b in range (0,4):
        tfr_byte(freq & 0xFF)
        freq=freq>>8
    tfr_byte(0x00)
    pulseHigh(FQ_UD)
    return




# start the DDS module
def start(frequency):
    pulseHigh(RESET)
    pulseHigh(W_CLK)
    pulseHigh(FQ_UD)
    sendFrequency(frequency)

# stop the DDS module
def stop():
    pulseHigh(RESET)
    



#fonction frere jacques sur la 4e octave    
def main():
    start(523)
    time.sleep(0.5)
    start(587)
    time.sleep(0.5)
    start(659)
    time.sleep(0.5)
    start(523)
    time.sleep(0.5)
    #1
    start(523)
    time.sleep(0.5)
    start(587)
    time.sleep(0.5)
    start(659)
    time.sleep(0.5)
    start(523)
    time.sleep(0.5)
    stop()
    #2
    time.sleep(0.1)
    start(659)
    time.sleep(0.5)
    start(698.5)
    time.sleep(0.5)
    start(784)
    time.sleep(0.7)
    stop()
    #3
    time.sleep(0.3)
    start(659)
    time.sleep(0.5)
    start(698.5)
    time.sleep(0.5)
    start(784)
    time.sleep(0.7)
    stop()
    #4
    time.sleep(0.3)
    start(784)
    time.sleep(0.4)
    start(880)
    time.sleep(0.15)
    start(784)
    time.sleep(0.3)
    start(698.5)
    time.sleep(0.3)
    start(659)
    time.sleep(0.5)
    start(523)
    time.sleep(0.5)
    stop()
    #5
    start(784)
    time.sleep(0.4)
    start(880)
    time.sleep(0.15)
    start(784)
    time.sleep(0.3)
    start(698.5)
    time.sleep(0.3)
    start(659)
    time.sleep(0.5)
    start(523)
    time.sleep(0.5)
    stop()
    #6
    time.sleep(0.2)
    start(523)
    time.sleep(0.6)
    start(392)
    time.sleep(0.6)
    start(523)
    time.sleep(0.6)
    stop()
    #7
    


if __name__ == '__main__':
    main()

   
    
