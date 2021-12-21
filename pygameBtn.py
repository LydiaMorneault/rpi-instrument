import RPi.GPIO as GPIO
import time
import pygame
import os
import numpy as np

moon = "spacesweep.flac"
swearnot = 'swear_not.wav'

pygame.mixer.init()
pygame.mixer.set_num_channels(3)

volume = 0.8

player = pygame.mixer.music

player.set_volume(0.5)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(23, GPIO.IN)

while True:
    # Button to trigger tones
    if GPIO.input(26) == False:
	num = np.random.randint(1,10)
	filename = str(num)+".wav"
	print(filename)

	pygame.mixer.Channel(2).play(pygame.mixer.Sound(filename))
    # force sensitive resistor
    if (GPIO.input(23) == GPIO.LOW):
	    pygame.mixer.Channel(1).play(pygame.mixer.Sound(swearnot))


