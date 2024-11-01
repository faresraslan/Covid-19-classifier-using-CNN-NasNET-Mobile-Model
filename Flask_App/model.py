import keras
import pandas as pd
import numpy as np
import tensorflow as tf


IMG_HEIGHT = 224
IMG_WIDTH = 224
BATCH_SIZE = 200

new_model=keras.models.load_model("C:/Users/ALARAFAT/Desktop/NasNetMobile(Team 5)/Flask_App/NasNetMobile .h5")

train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    brightness_range=(1.2, 1.5),
    horizontal_flip=True
)

def img_re(x):
   imge = train_datagen.flow_from_directory(
    x,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    class_mode='binary',
    batch_size=BATCH_SIZE)   
   return imge
   
#x='C:/Users/ALARAFAT/Desktop/test/cs'

def predict(img):
    pred_labelss = np.squeeze(np.array(new_model.predict(img) >= 0.5, dtype=np.int))
    return pred_labelss

#y = img_re(x)
#z =predict(y)

#if z==0:
 #print("normal")
#else:
 #   print("you have corona ")
