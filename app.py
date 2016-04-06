#!/usr/bin/python
# By Azores
#this scripts quick and dirty assumes 	- that the mp3 filesare named like this: "music_[1-9].mp3"
#					- the notes are on the pins 1 -> NB_INPUT, on Board mode
#					- NB_INPUTS are normal notes, NB_INPUT+1 is a trap key and NB_INPUT+2 is a "turn off" key
# we might have a problem. This only detects rising signals, so the sound will play at rising. What happens if the user maintains the key and the mp3 is over?
#TODO: change the above problem



import RPi.GPIO as GPIO
import pygame	#to play audio files

NB_INPUT = 8			#GPIO correspondants a des notes
SEQUENCE = [3,3,8,7,8,7,3]	#notes a jouer sous forme des pin qui rentrent. ATTENTION, pas mettre de num > NB_INPUT
user_input = []     #notes jouees par l utilisateur
available_gpio=[3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26]

GPIO.setmode(GPIO.BOARD)	#on identifie les GPIO par leurs place sur la board

def play_sound(music_file):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():	#might not be necesary (might actualy be a bug, to test)
        continue

def my_callback(channel):  #not sure what the paramater channel represents
    global user_input
    for i in range(0,NB_INPUT+1):
        if GPIO.input(available_gpio[i]):
            music_file = "music_"+str(i)+".mp3"
            play_sound(music_file)
            if (len(user_input) == 0 and SEQUENCE[0] == available_gpio[i]) or (available_gpio[i] == SEQUENCE[len(user_input)]):		#la note est bonne len(user_input)+1?
                if SEQUENCE == user_input: #cest gagne
                    print "Cest gagne, c est gagne" #mp3 de dora l'exploratrice?
                    user_input = []	#reset the game
                #put GREEN lights!
                else:
                    user_input.append(available_gpio[i])
            else:
                if i == NB_INPUT+1: #si on a appuye sur la touche piege
                    #play_sound("cest_un_piege.mp3")
                    pass
                user_input = []	#on vide les trucs entre par l'utilisateur


try:
    for i in range(0, NB_INPUT+2):  #+1 pour le io "piege", +1 pour "turn off"
        GPIO.setup(available_gpio[i], GPIO.IN)		#on declare les io comme des user_input
        GPIO.add_event_detect(available_gpio[i], GPIO.RISING, callback=my_callback)		#on leur ajoute leur listener

    while True:
        if GPIO.input(available_gpio[NB_INPUT+2]):	#if turn off
            break
        pass
finally:
    GPIO.cleanup()
