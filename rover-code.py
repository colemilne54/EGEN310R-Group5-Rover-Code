import curses
from pololu_drv8835_rpi import motors, MAX_SPEED
import time
 
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
 
def forwards(spd):
	motors.setSpeeds(-spd, -spd)
 
def backwards(spd):
	forwards(-spd)
 
def right(spd):
	motors.setSpeeds(0,-spd)
 
def left(spd):
	motors.setSpeeds(-spd, 0)
 
def stop():
	motors.setSpeeds(0,0)
 
def sleepOne():
	time.sleep(1)


try:
	while True:
		char = screen.getch()
		print("after char")
		if char == ord('p'):
			break
		elif char == ord('w'):
			forwards(200)
			sleepOne()
			stop()
		elif char == ord('s'):
			backwards(200)
			sleepOne()
			stop()
		elif char == ord('a'):
			left(100)
			sleepOne()
			stop()			
		elif char == ord('d'):
			right(100)
			sleepOne()
			stop()
		elif char == ord('i'):
			forwards(300)
			sleepOne()
			stop()
		elif char == ord('k'):
			backwards(300)
			sleepOne()
			stop()
 
 
finally:
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()