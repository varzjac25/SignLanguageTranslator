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

# loop continously runs until broken
while True:

    # if video is true record and call hand tracker class
    if video:

        # read camera input
        success, image = cam.read()

        # calls trackHands from HandTracker class
        trackHands(readASL, showPoints, image)

    # if foreign is true call ForeignLanguageTranslation to translate
    elif foreign:

        # call translateForeign from ForeignLanguageTranslation Class
        # first parameter is input text, second parameter is output language

        # test case 1
        txt = "buenas dias mi amigo"
        language = "EngLiSh"
        print(translateForeign(txt, language))

        # test case 2
        txt = "good morning my friend"
        language = "chineSE"
        print(translateForeign(txt, language))

        # test case 3
        txt = "buenas dias mi amigo"
        language = "xxx"
        print(translateForeign(txt, language))

        break

    else:
        break

# After the loop release the cap object
cam.release()

# Destroy all the windows
cv2.destroyAllWindows()