#Main file for Robotic Musicianship Group project 
#Group members
#Rhythm Jain
#Nitin Hugar
#Keith Ng

from .utils import Utils
from .rtpmidi_handler import MyHandler
from .rtpmidi import RtpMidi
import RPi.GPIO as GPIO
from .utils import DATA, LATCH, CLOCK, PUMP

# TODO : MAKE A FOOLPROOF FOR POLYPHONY MORE THAN 4
# TODO : Handle note ranges
# TODO: Handle cc ranges 

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DATA,GPIO.OUT)
    GPIO.setup(LATCH,GPIO.OUT)
    GPIO.setup(CLOCK,GPIO.OUT)
    GPIO.setup(PUMP,GPIO.OUT)

if __name__ == '__main__':

	# initialize raspberry pi 
	setup()

	# initialize midi server
	ROBOT = "Your Robot"
	PORT = 5004
	rtp_midi = RtpMidi(ROBOT, MyHandler(), PORT)
	rtp_midi.run()


	



