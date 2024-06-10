# Main runs other python classes based off user input,
# uses other classes to translate from different language mediums

# imports
import cv2
from HandTracker import *
from ForeignLanguageTranslation import *
from AudioTranslation import *

# declare variables
video = False
readASL = True
showPoints = False
foreign = True

# initialize camera
cam = cv2.VideoCapture(0)

# get translation type
trans = input("Translate From: ")[0:3].lower()
transTo = input("Translate To: ")[0:3].lower()

# if translation type is vid prepare data
if trans == "asl" or trans == "vid":
    sameLetter = 0
    firstLetter = True
    oldLetter = ''
    letter = ''

# message in english is the message that will be translated
messageInEnglish = ""

if trans == "eng":
    messageInEnglish = input("Enter message: ")

# loop continously runs until broken
while True:

    # q breaks loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # if translation type is vid record and call hand tracker class
    if trans == "asl" or trans == "vid":

        # read camera input
        success, image = cam.read()

        # calls trackHands from HandTracker class
        letter = trackHands(readASL, showPoints, image)

        # set oldLetter to letter if its the first runthrough of the loop
        if firstLetter:

            # print letter
            firstLetter = False
            oldLetter = letter
            print(letter)

        # print letter if it is a new letter or has been held up for long enough
        if oldLetter != letter:
            messageInEnglish += letter
        elif sameLetter >= 100:
            messageInEnglish += letter
            sameLetter = 0
        else:
            sameLetter += 1

        if letter == "delete":
            break

    # if foreign is true call ForeignLanguageTranslation to translate
    elif trans == "for":

        # call translateForeign from ForeignLanguageTranslation Class
        # first parameter is input text, second parameter is output language

        # get text input from user
        txt = input("Text (type /q to quit): ")

        # break for loop based on user inputsa
        if txt == "/q":
            break
        else:
            # relay user input to foreign language translation
            language = input("Translate to: ")
            print(translateForeign(txt, language))

    # if translation type is audio call AudioTranslation to translate
    elif trans == "aud":

        # save message in english
        messageInEnglish = recordText()
        break

    else:
        break

# print messageInEnglish in selected translation type
if transTo == "eng":
    print(messageInEnglish)
elif transTo == "aud":
    outputAudio(messageInEnglish)

# After the loop release the cap object
cam.release()

# Destroy all the windows
cv2.destroyAllWindows()