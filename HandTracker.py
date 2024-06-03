# Jackson Varzali
# HandTracker uses google mediapipe to track hands from still frames
# captured from a video

# imports
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cv2
from SignLanguageRecognition import *

# method is called from main
def trackHands(read, points, image):

    # initialize variables
    crop = False
    width, height = 0, 0

    # readASL variable runs SignLanguageRecognition when set to true
    # showPoints shows hand tracking keypoints when set to true
    readASL = True
    showPoints = False
    img1 = image

    # initialize hand tracker
    tracker = HandDetector(False, 2, 1, 0.5, 0.5)

    # loop continously runs
    # while True:

    # get width and height of image
    width, height = img1.shape[:2]

    # read hand input
    hands, img = tracker.findHands(img1, True, True)

    # check if any hands are detected
    if hands:

        # assign hand1 to first hand detected
        hand1 = hands[0]

        # list of points of landmarks on hand
        lmlist1 = hand1["lmList"]

        # print lmlist1
        #print(lmlist1)

        # check for second hand
        if len(hands) > 1 and not crop:
            # assign hand2 to second hand detected
            hand2 = hands[1]

            # list of points of landmarks on second hand
            lmlist2 = hand2["lmList"]

        # if crop is turned on crop out everything other than hand
        if crop:

            # max and min variables to determine area to be cropped
            maxX = 0
            maxY = 0
            minX = width
            minY = height

            # loop through coordinates of hand and save min/max coordinates to each point
            for x, y, z in lmlist1:
                if x > maxX:
                    maxX = x
                if y > maxY:
                    maxY = y
                if x < minX:
                    minX = x
                if y < minY:
                    minY = y

            # set min and max points so cropped image is larger
            minX -= 100
            minY -= 100
            maxX += 100
            maxY += 100

            # make sure points are in bounds
            if minX < 0:
                minX = 0
            if minY < 0:
                minY = 0
            if maxX > width:
                maxX = width
            if maxY > height:
                maxY = height

            # set points list to crop image using min and max cords
            newPoints = np.int32([[minX, minY], [maxX, maxY]])

            # print new points
            print(newPoints)

            # crop image
            if maxX > minX and maxY > minY:
                img = img[minY: maxY, minX: maxX]

    # show the image if readASL is false
    if not readASL:
        # display image with keypoints
        cv2.imshow("image", img)
    else:
        # display image with or without keypoints based on showPoints
        if showPoints:
            readCurrentLetter(img)
        else:
            readCurrentLetter(img1)

    # q crops/uncrops image
    if cv2.waitKey(1) & 0xFF == ord('q'):
        crop = not crop
        print(crop)
