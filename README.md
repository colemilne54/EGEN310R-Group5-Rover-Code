# EGEN310R Group5 Rover Code

## Overview
The main idea of our rover code is that the curses and pololu_drv8835_rpi libraries are used in conjunction to take keyboard input and translate that into motor movement.

## Structure
### Functions
#### forwards(spd)
Takes a value 1-400 to control the speed of forwards movement (one keypress is a second of forwards movement)

#### backwards(spd)
Takes a value 1-400 to control the speed of backwards movement (one keypress is a second of backwards movement)
 
#### right(spd)
Takes a value 1-400 to control the speed of a right turn (one keypress is a second of right turning)
 
#### left(spd)
Takes a value 1-400 to control the speed of a left turn (one keypress is a second of left turning)

#### stop()
Sets both motors' speed to 0 (stopping them)

#### sleepOne()
Pauses code execution for 1 second

### Main Loop
Curses is used to wait for keyboard input and run corresponding functions (see above) for rover control
