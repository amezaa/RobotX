import pandas as pd

import buildcolordataset
dataset = pd.read_csv('../Datasets/colors.csv').values

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

import matplotlib.pyplot as plt

#visualize colors on scatterplot 
# blues = dataset[dataset[:,-1] == 'blue']
# reds = dataset[dataset[:,-1] == 'red']
# greens = dataset[dataset[:,-1] == 'green']

#begin data analysis
x = dataset[:,:-1]
y = dataset[:, -1]

#transform data labels into integers
label_encoder = LabelEncoder()
label_encoded_y = label_encoder.fit_transform(y)

#split data for training & testing
x_training, x_test, y_training, y_test = train_test_split(x,label_encoded_y, test_size=0.33)

#Classifier : KNN
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(x_training, y_training)

#analyze predictions
y_pred = knn.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy KNN: %.2f%%" % (accuracy * 100.0))

import numpy as np

#given input point , predict output
def pred(my_point_r, my_point_g, my_point_b):
    my_point = np.array([my_point_r, my_point_g, my_point_b])[:, np.newaxis].T

    my_predicted_point = knn.predict(my_point)
    print(label_encoder.inverse_transform(my_predicted_point))

