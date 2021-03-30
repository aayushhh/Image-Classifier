#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:34:50 2020

@author: Aayush
"""


import numpy as np
import glob, os, csv, ntpath
import tensorflow as tf
import efficientnet.tfkeras
from tensorflow.keras.models import load_model

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def preprocessing_img(img_path):
    #Converting the image to tensor
    img = tf.keras.preprocessing.image.load_img(img_path, target_size = (224, 224), interpolation = "lanczos")
    #this function Loads the image and resizes it to the specified size using PIL(Nearest Neighbour)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    #this function converts the image to numpy Array
    img_array = np.expand_dims(img_array, axis=0)
    #(1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_array /= 255.
    #the numpy array are normalized between 0 and 1
    return img_array



main_dir = "../production_data/nov_week3/"

real_images = glob.glob(main_dir + "images/temp/real/*")
fake_images = glob.glob(main_dir + "images/temp/fake/*")

all_images = real_images + fake_images

output_file = open(main_dir + 'scores.csv', 'w', newline='')
row = ['date', 'image_name', 'gt', 'pred', 'score']
csv_writer  = csv.writer(output_file)
csv_writer.writerow(row)


model_path = "../models/Dkyc/Server/Customer/prodcution_ready/bs16_001faceliveness_v_0_108-0p97.h5"
model = tf.keras.models.load_model(model_path)
model.summary()

real_pred_count = 0
fake_pred_count = 0
err_count = 0
thresh = 0.5

for image_path in all_images[:]:
    
    # dir_date = os.path.basename(os.path.dirname(os.path.dirname(image_path)))
    dir_name = os.path.basename(os.path.dirname(image_path))
    filename = path_leaf(image_path)
    
    preproc_image = preprocessing_img(image_path)
    pred = model.predict(preproc_image)
    
    if dir_name == "real" and pred >= thresh:
        real_pred_count += 1
        pred_val = "real"
        
    elif dir_name == "real" and pred < thresh:
        pred_val = "fake"
        
    elif dir_name == "fake" and pred < thresh:
        fake_pred_count += 1
        pred_val = "fake"
        
    elif dir_name == "fake" and pred > thresh:
        pred_val = "real"
    
    
    row = ["dir_date", filename, dir_name, pred_val, pred[0]]
    csv_writer.writerow(row)
        
print("no.of errors", err_count)
output_file.close()

real_acc = (real_pred_count / len(real_images)) * 100
fake_acc = (fake_pred_count / len(fake_images)) * 100

print("Real Accuracy: {} / {} = {:.2f}%".format(real_pred_count, len(real_images), real_acc))
print("Fake Accuracy: {} / {} = {:.2f}%".format(fake_pred_count, len(fake_images), fake_acc))



