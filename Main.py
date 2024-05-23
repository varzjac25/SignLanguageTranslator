# Jackson Varzali
# Main runs other python classes based off user input,
# uses other classes to translate from different language mediums

# imports
import cv2
from HandTracker import *
from ForeignLanguageTranslation import *

# declare variables
video = False
readASL = True
showPoints = False
foreign = True

# initialize camera
cam = cv2.VideoCapture(0)

# get translation type
trans = input("Translate From: ")[0:3].lower()

# loop continously runs until broken
while True:

    # if video is true record and call hand tracker class
    if trans == "asl" or trans == "vid":

        # read camera input
        success, image = cam.read()

        # calls trackHands from HandTracker class
        trackHands(readASL, showPoints, image)

    # if foreign is true call ForeignLanguageTranslation to translate
    elif trans == "for":

        # call translateForeign from ForeignLanguageTranslation Class
        # first parameter is input text, second parameter is output language

        # get text input from user
        txt = input("Text (type /q to quit): ")

        # break for loop based on user input
        if txt == "/q":
            break
        else:
            # relay user input to foreign language translation
            language = input("Translate to: ")
            print(translateForeign(txt, language))

    else:
        break

# After the loop release the cap object
cam.release()

# Destroy all the windows
cv2.destroyAllWindows()