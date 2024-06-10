# SignLanguageRecognition translates images of the American Sign Language Alphabet
# into english text using machine learning

# imports
import os
import cv2
import numpy as np
import pickle
import matplotlib.pyplot as plt

# science kit imports
from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# prepare data for image recogniton
input_dir = 'C:/Users/JVarz/Documents/GitHub/SignLanguageTranslator/asl_alphabet_train'
categories = ["A", "B", "C", "D", "del", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "nothing", "O", "P", "Q",
              "R", "S", "space", "T", "U", "V", "W", "X", "Y", "Z"]

# create variables
data = []
labels = []

# traverse through data saved in computer
a = 0
for category_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, category)):
        a += 1
        # get image and resize it
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        img = resize(img, (15, 15))

        # store a simplfied image and its category to lists
        data.append(img.flatten())
        labels.append(category)
        print(a)
        print (str(category) + " " + str(img.flatten())[0:10])

# cast lists to np array
data = np.asarray(data)
labels = np.asarray(labels)
print (len(data))
print (len(labels))

# split data into 80% train 20% test datasets
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size = 0.2, shuffle = True, stratify = labels)
print("finished splitting")

# classifier object to train object classifier
classifier = SVC()
print("finished creating classifier object")

# parameters will be used to train multiple image classifiers with selecte C and Gamma values
# 12 image classifiers will be trained: 3x4=12
parameters = [{'gamma': [0.01, 0.001, 0.0001,], 'C': [1, 10, 100, 1000]}]
print("finished creating parameters")

# create image classifiers using parameters
grid_search = GridSearchCV(classifier, parameters)
print("creating image classifier step 1 finished")
grid_search.fit(x_train, y_train)
print("creating image classifier step 2 finished")

# test performance of image classifier
best_estimator = grid_search.best_estimator_
print("machine learning object created")
y_prediction = best_estimator.predict(x_test)
score = accuracy_score(y_prediction, y_test)


# print accuracy of image classifier
print('{}% of samples were correctly classified'.format(str(score*100)))

# create file of image classifier
pickle.dump(best_estimator, open('SignLanguageRecognition.pickle', 'wb'))