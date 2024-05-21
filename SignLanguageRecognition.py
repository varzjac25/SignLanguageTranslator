# Jackson Varzali
# SignLanguageRecognition translates images of the American Sign Language Alphabet
# into english text using machine learning

# imports
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
# import tensorflow as tf

# read current letter uses ai to translate the American Sign Language Alphabet to text
def readCurrentLetter(img):

    # will recognize the sign language alphabet when complete

    # asl_alphabet_train is the dataset that will be used for language recognition

    # display image
    cv2.imshow("image", img)