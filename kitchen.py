#!/usr/bin/env python3

import signal
import sys
import RPi.GPIO as GPIO
from pygame import mixer

BUTTON_GPIO = 16

#mixer.init()
#mixer.music.load('43010136_sink-filling-with-water-01.mp3')

def signal_handler(sig, frame):
    GPIO.cleanup()
    mixer.quit()
    sys.exit(0)

def play(channel):
    if GPIO.input(channel):
        print("Button pressed!")
        mixer.init()
        mixer.music.set_volume(0.3)
        mixer.music.load('43010136_sink-filling-with-water-01.mp3')
        mixer.music.play()
    else:
        print("Button released!")
        mixer.music.stop()
        mixer.quit()

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, 
            callback=play, bouncetime=500)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
