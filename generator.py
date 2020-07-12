# import GUI module
from tkinter import *

# import GPIO module
import RPi.GPIO as GPIO

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


# Class definition for RPiRFSigGen application
class RPiRFSigGen:
        # Build Graphical User Interface
        def __init__(self, master):
                frame = Frame(master, bd=10)
                frame.pack(fill=BOTH,expand=1)
                # set output frequency
                frequencylabel = Label(frame, text='Frequency (Hz)', pady=10)
                frequencylabel.grid(row=0, column=0)
                self.frequency = StringVar()
                frequencyentry = Entry(frame, textvariable=self.frequency, width=10)
                frequencyentry.grid(row=0, column=1)
                # Start button
                startbutton = Button(frame, text='Start', command=self.start)
                startbutton.grid(row=1, column=0)
                # Stop button
                stopbutton = Button(frame, text='Stop', command=self.stop)
                stopbutton.grid(row=1, column=1)


        # start the DDS module
        def start(self):
                frequency = int(self.frequency.get())
                pulseHigh(RESET)
                pulseHigh(W_CLK)
                pulseHigh(FQ_UD)
                sendFrequency(frequency)

        # stop the DDS module
        def stop(self):
                pulseHigh(RESET)

# Assign TK to root
root = Tk()

# Set main window title
root.wm_title('RPi RFSigGen')

# Create instance of class RPiRFSigGen
app = RPiRFSigGen(root)

# Start main loop and wait for input from GUI
root.mainloop()
