import RPi.GPIO as GPIO         ## Import GPIO Library
import time                     ## Import 'time' library (for 'sleep')
 
outPin = 13                      ## LED connected to pin 7
inPin = 7                      ## Switch connected to pin 13
GPIO.setmode(GPIO.BOARD)        ## Use BOARD pin numbering
GPIO.setup(outPin, GPIO.OUT)    ## Set pin 7 to OUTPUT
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)      ## Set pin 13 to INPUT
 
while True:                     ## Do this forever
    value = GPIO.input(inPin)   ## Read input from switch
    if value:                   ## If switch is released
        print "pressed"
	GPIO.output(outPin, 0)  ## Turn off LED
    else:                       ## Else switch is pressed
        GPIO.output(outPin, 1)  ## Turn on LED
 
GPIO.cleanup() 
