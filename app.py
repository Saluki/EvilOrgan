#!/usr/bin/python
# By Azores

import RPi.GPIO as GPIO  
import pygame	#to play audio files

NB_INPUT = 8
SEQUENCE = [3,2,3,3,6,5,3]	#notes a jouer sous forme des pin qui rentrent. ATTENTION, pas mettre de num > NB_INPUT
input = []	#notes jouees par l utilisateur

GPIO.setmode(GPIO.BOARD)

def playSound(file):
	pygame.mixer.init()
	pygame.mixer.music.load(music_file)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:	#might not be necesary (might actualy be a bug, to test)
		continue

def my_callback(channel):  
	global input
	for i in range(1,NB_INPUT+1):
		if GPIO.input(i):
			music_file = "music_"+str(i)+".mp3"
			playSound(music_file)
    		if (len(input) == 0 and SEQUENCE[0] == i) or (i == SEQUENCE[len(input)-1]):		#la note est bonne
    			if SEQUENCE == input: #cest gagne
    				print "Cest gagné, c est gagné" #mp3 de dora l'exploratrice?
    		else:
    			input = []	#on vide les trucs entré par l'utilisateur


try:
	for i in range(1, NB_INPUT+3):  #+1 pour le io "piege", +1 pour "turn off"
		GPIO.setup(i, GPIO.IN)		#on declare les io comme des input
		GPIO.add_event_detect(i, GPIO.RISING, callback=my_callback)		#on leur ajoute leur listener
		
	while true:
		if GPIO.input(NB_INPUT+1):	#if turn off
			break
		pass
finally:
	GPIO.cleanup()
