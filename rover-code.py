print("before imports")
 
import curses
from pololu_drv8835_rpi import motors, MAX_SPEED
import time
 
print("before screen")
 
screen = curses.initscr()
print("1")
curses.noecho()
print("2")
curses.cbreak()
print("3")
screen.keypad(True)
 
print("before defs")
 
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
 
print("before try")
 
 
 
try:
	while True:
		print("before char")
		char = screen.getch()
		#char = input()
		print("after char")
		if char == ord('p'):
		#if char == 'p':
			break
		elif char == ord('w'):
		#elif char == 'w':
			forwards(200)
			sleepOne()
			stop()
		elif char == ord('s'):
		#elif char == 's':
			backwards(200)
			sleepOne()
			stop()
		elif char == ord('a'):
		#elif char == 'a':
			left(400)
			sleepOne()
			stop()			
		elif char == ord('d'):
		#elif char == 'd':
			right(400)
			sleepOne()
			stop()	
 
 
finally:
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()