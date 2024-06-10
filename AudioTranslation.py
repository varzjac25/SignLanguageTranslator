# AudioTranslation translates audio into text and text into audio

# imports
import speech_recognition as sr
import pyttsx3
import pyaudio
from gtts import gTTS
import os

# initialize recognizer
r = sr.Recognizer()

# record text translates audio into text
def recordText():
    # loop until audio is recognized
    while True:
        # check if audio can be converted into text
        try:

            # use microphone for input
            with sr.Microphone() as source:

                # prepare recognizer to recieve input
                r.adjust_for_ambient_noise(source, duration = 0.2)

                # listen for user input
                audio = r.listen(source)

                # use google to recognize audio
                text = r.recognize_google(audio)

                # return text
                return text

        # if audio cannot be converted print error message
        except sr.RequestError:
            print("No speech detected")
        except sr.UnknownValueError:
            print("No speech detected")

# output audio converts text into audio
def outputAudio(input):

    # output audio using gTTS
    audio = gTTS(text = input, lang = 'en', slow = False)

    # save and play audio file
    audio.save("temp.mp3")
    os.system("start temp.mp3")
