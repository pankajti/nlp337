from sklearn import *
from tensorflow import keras as keras
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical

import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.datasets import load_digits

import requests
from bs4 import BeautifulSoup


def question1_a():
    digits = load_digits()
    X, y = load_digits(return_X_y=True)
    model = keras.Sequential()
    one_hot_train_labels = to_categorical(y)
    #one_hot_test_labels = to_categorical(test_labels)
    model.add(layers.Dense(64, activation='relu', input_shape=(64,)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
    history = model.fit(X, one_hot_train_labels, epochs=10, batch_size=20)
    print(digits.DESCR)

#ii = list(map(print ,[[elem[i] for i in [0,4,5]] for elem in [elems.text.strip().split('\n')  for elems in BeautifulSoup(requests.get('https://www.billboard.com/charts/hot-100').text).find_all(class_='chart-element__wrapper')]]))
def question_2():
    response  = requests.get('https://www.billboard.com/charts/hot-100')
    soup = BeautifulSoup(response.text)

    elemnts  =[elems.text.strip().split('\n')  for elems in soup.find_all(class_='chart-element__wrapper')]
    records =[[elem[i] for i in [0,4,5]] for elem in elemnts]
    print(records)
    return records

question_2()