import time
import RPi.GPIO as GPIO
from pygame import mixer

# Pins definitions
btn_pin = 17
i = 0
# Set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize pygame mixer
#mixer.init()

# Remember the current and previous button states
current_state = True
prev_state = True
def play(soundfile, duration_secs):
    """Play a soundfile for a configurable duration"""

    mixer.init()
    mixer.music.load(soundfile)
    mixer.music.play()
    time.sleep(duration_secs)
    mixer.music.stop()
    mixer.quit()

# Load the sounds

# If button is pushed, light up LED
try:
    while True:
        current_state = GPIO.input(btn_pin)
        if (current_state == True):
            print("TTTT")
            play('43010136_sink-filling-with-water-01.mp3',10)
            print("wefwef")
        prev_state = current_state
        i=i+1
        print(i)
        time.sleep(0.2)

# When you press ctrl+c, this will be called
finally:
    GPIO.cleanup()
