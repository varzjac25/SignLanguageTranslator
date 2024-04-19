# imports
from cvzone.HandTrackingModule import HandDetector
import cv2

# initialize camera
cam = cv2.VideoCapture(0)

# initialize hand tracker
tracker = HandDetector(False, 2, 1, 0.5, 0.5)
# tracker = HandDetector(maxHands=2, detectionCon=0.8)
while True:

    # read camera input
    success, img = cam.read()

    # read hand input
    hands, img = tracker.findHands(img, True, True)
    # hands, img = tracker.findHands(img)

    # check if any hands are detected
    if hands:

        # assign hand1 to first hand detected
        hand1 = hands[0]

        # list of points of landmarks on hand
        lmlist1 = hand1["lmList"]

        # print lmlist1
        print(lmlist1)

        # check for second hand
        if len(hands) > 1:
            # assign hand2 to second hand detected
            hand2 = hands[1]

            # list of points of landmarks on second hand
            lmlist2 = hand2["lmList"]

            # show the image
    cv2.imshow("image", img)

    # q breaks from loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cam.release()
# Destroy all the windows
cv2.destroyAllWindows()