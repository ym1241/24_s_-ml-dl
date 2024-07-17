# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:28:51 2024

@author: kim
"""


import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential

inputs = np.random.random([32,3,1]).astype(np.float32)
model = Sequential()
model.add(tf.keras.layers.SimpleRNN(
    3, input_shape=(32,1)))
model.summary()