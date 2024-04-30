# imports
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cv2

# initialize camera
cam = cv2.VideoCapture(0)

# initialize variables
crop = True
width, height = 0, 0

# initialize hand tracker
tracker = HandDetector(False, 2, 1, 0.5, 0.5)

# tracker = HandDetector(maxHands=2, detectionCon=0.8)
while True:

    # read camera input
    success, img = cam.read()

    # get width and height of image
    width, height = img.shape[:2]

    # read hand input
    hands, img = tracker.findHands(img, True, True)

    # check if any hands are detected
    if hands:

        # assign hand1 to first hand detected
        hand1 = hands[0]

        # list of points of landmarks on hand
        lmlist1 = hand1["lmList"]

        # print lmlist1
        print(lmlist1)

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
            minX -= 50
            minY -= 50
            maxX += 50
            maxY += 50

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

            # crop image
            if maxX > minX and maxY > minY:
                img = img[minY: maxY - minY, minX: maxX - minX]

    # show the image
    cv2.imshow("image", img)

    # q breaks from loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # e crops video to show only the hand
    # if cv2.waitKey(1) & 0xFF == ord('e'):
    #     crop = not crop
    #     print (crop)

# After the loop release the cap object
cam.release()
# Destroy all the windows
cv2.destroyAllWindows()