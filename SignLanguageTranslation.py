# SignLanguageTranslation translates American Sign Language
# into text using sign language recognition machine learning

# imports
import pickle
from skimage.transform import resize
import numpy as np
import cv2

# load machine learning model
MODEL = pickle.load(open('SignLanguageRecognition.pickle', 'rb'))

# translate translates image of ASL into a letter
def translate(img):

    # create variables
    flat_data = []

    # resize image and append to numpy array
    img_resized = resize(img, (15, 15, 3))
    flat_data.append(img_resized.flatten())
    flat_data = np.asarray(flat_data)

    # get predicted letter
    y_output = MODEL.predict(flat_data)

    # return letter
    return y_output