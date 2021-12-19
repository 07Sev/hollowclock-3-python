#    Hollowclock 3 for raspberry pi pico. Drives the steppermotor and keeps time.
#    Copyright (C) 2021  David Weijzen
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


#PRINT LISCENSE INFORMATION IN TERMINAL:
print("Hollowclock3 for micropython  Copyright (C) 2021  David Weijzen")
print("This program comes with ABSOLUTELY NO WARRANTY")
print("This is free software, and you are welcome to redistribute it under certain conditions")

#Setup:
from machine import Pin
import utime


#global variables
global motorPins
phase = 0
motorPins = [6,7,8,9]
stepsPerRotation = 56320
minutesPassed = 0


led = Pin(25,Pin.OUT)
motorPin0 = Pin(6,Pin.OUT)
motorPin1 = Pin(7,Pin.OUT)
motorPin2 = Pin(8,Pin.OUT)
motorPin3 = Pin(9,Pin.OUT)
print("Pins have been set up!")



sequence = [[0,1,1,0],
         [0,0,1,0],
         [0,0,1,1],
         [0,0,0,1],
         [1,0,0,1],
         [1,0,0,0],
         [1,1,0,0],
         [0,1,0,0]]

def rotateMotor(amoundOfSteps):
    print("Entering rotateMotor Function")
    timeDelayMS = 1
    global phase
    
    for i in range(amoundOfSteps):
        if (phase > 7):
            phase = 0
        delta = 0
        motorPin0.value(sequence[phase][delta])
        delta = delta + 1
        motorPin1.value(sequence[phase][delta])
        delta = delta + 1
        motorPin2.value(sequence[phase][delta])
        delta = delta + 1
        motorPin3.value(sequence[phase][delta])
        utime.sleep_ms(timeDelayMS)
        phase = phase + 1
    
    motorPin0.off()
    motorPin1.off()
    motorPin2.off()
    motorPin3.off()
    
#Loop:
print("Entering Loop")
while (True):
    rotateMotor(938)
    minutesPassed = minutesPassed + 1
    print("1 minute has passed")
    utime.sleep_ms(59022)
    if (minutesPassed == 60):
        minutesPassed = 0
        rotateMotor(40)
        print("Compensated minute rotor for hour")
    else:
        utime.sleep_ms(40)
        
    