import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.OUT)

btn1_button = 'up'
btn1_light = 'off'

def LED1(output):
	GPIO.output(11, output)
while True:
######################## BUTTON 1 ########################
	if (btn1_button == 'up' and btn1_light == 'off'):
		if not  GPIO.input(7):
			print "LED1 ON"
			LED1(1)         
			btn1_button = 'down'
			btn1_light = 'on'
	elif (btn1_button == 'down' and btn1_light == 'on'):
		if GPIO.input(7):
			btn1_button = 'up'
	elif (btn1_button == 'up' and btn1_light == 'on'):
		if not GPIO.input(7):
			print "LED1 OFF"
			LED1(0)
			btn1_button = 'down'
			btn1_light = 'off'
	elif (btn1_button == 'down' and btn1_light == 'off'):
		if GPIO.input(7):
			btn1_button = 'up'
	sleep(0.1)
###########################################################

GPIO.cleanup()
