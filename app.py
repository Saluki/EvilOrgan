#!/usr/bin/python
# By Azores
#this scripts quick and dirty assumes 	- that the mp3 filesare named like this: "music_[1-9].mp3"
#					- the notes are on the pins 1 -> NB_INPUT, on Board mode
#					- NB_INPUTS are normal notes, NB_INPUT+1 is a trap key and NB_INPUT+2 is a "turn off" key
# we might have a problem. This only detects rising signals, so the sound will play at rising. What happens if the user maintains the key and the mp3 is over?
#TODO: change the above problem
#TODO: add a function reseting the input



import RPi.GPIO as GPIO  
import pygame	#to play audio files

NB_INPUT = 8			#GPIO correspondants a des notes
SEQUENCE = [3,2,3,3,6,5,3]	#notes a jouer sous forme des pin qui rentrent. ATTENTION, pas mettre de num > NB_INPUT
input = []			#notes jouees par l utilisateur

GPIO.setmode(GPIO.BOARD)	#on identifie les GPIO par leurs place sur la board

def play_sound(file):
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:	#might not be necesary (might actualy be a bug, to test)
		continue

def my_callback(channel):  #not sure what the paramater channel represents
	global input
	for i in range(1,NB_INPUT+1):
		if GPIO.input(i):
			music_file = "music_"+str(i)+".mp3"	
			play_sound(music_file)
	    		if (len(input) == 0 and SEQUENCE[0] == i) or (i == SEQUENCE[len(input)-1]):		#la note est bonne
	    			if SEQUENCE == input: #cest gagne
	    				print "Cest gagné, c est gagné" #mp3 de dora l'exploratrice?
	    				input = []	#reset the game
	    				#put GREEN lights!
	    			else:
	    				input.append(i)
	    		else:
	    			if i == NB_INPUT+2:#si on a appuyé sur la touche piège
	    				#play_sound("cest_un_piege.mp3")
	    				
	    			input = []	#on vide les trucs entré par l'utilisateur


try:
	for i in range(1, NB_INPUT+3):  #+1 pour le io "piege", +1 pour "turn off"
		GPIO.setup(i, GPIO.IN)		#on declare les io comme des input
		GPIO.add_event_detect(i, GPIO.RISING, callback=my_callback)		#on leur ajoute leur listener
		
	while true:
		if GPIO.input(NB_INPUT+2):	#if turn off
			break
		pass
finally:
	GPIO.cleanup()
