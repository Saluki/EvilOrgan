import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)

n=0

try:
	while True:
		input_state = GPIO.input(7)
		if input_state:
			print('Button Pressed')
			if n==0:
				print "led HIGH"
				GPIO.output(11, GPIO.HIGH)
				n = 1
			else :
				print "LED low"
				GPIO.output(11,GPIO.LOW)
				n = 0
			time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
