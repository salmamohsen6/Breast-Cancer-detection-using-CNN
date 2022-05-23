# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 03:03:19 2020

@author: HP.SXO7
"""


import sys
from os.path import join
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.python.keras.applications.resnet50 import preprocess_input
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
#from tensorflow.python.keras.applications import ResNet50

from keras import models, regularizers, layers, optimizers, losses, metrics
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils, to_categorical
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications import ResNet50

import os

# Convoluted Base MODEL

conv_base = ResNet50(weights='imagenet',include_top=False, input_shape=(224, 224, 3))

print(conv_base.summary())


model = models.Sequential()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dropout(0.5))
model.add(layers.Dense(64, activation='relu',kernel_regularizer=regularizers.l2(0.001)))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(5, activation='sigmoid'))

print(model.summary())

for layer in conv_base.layers[:]:
   layer.trainable = False

print('conv_base is now NOT trainable')


for i, layer in enumerate(conv_base.layers):
   print(i, layer.name, layer.trainable)
   
   
   
model.compile(optimizer=optimizers.Adam(),
              loss='binary_crossentropy',
              metrics=['accuracy'])

print("model compiled")
print(model.summary())