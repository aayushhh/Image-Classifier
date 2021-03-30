#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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

#model = "/home/aayush/Documents/liveness/models/Dkyc/Server/Customer/vamshi/layer_finetuned_unfrozen_adam_weights-improvement-face_liveness_v_2_0_224_224_sgd08-0.98485.h5"
#model = "/home/aayush/Documents/liveness/models/Dkyc/Server/Agent/New_puru_Agent_Nima_exp1_weight-004-0.97567.h5"
model = "/home/aayush/Documents/liveness/models/Dkyc/Server/Agent/New_puru_Agent_Nima_exp1_weight-004-0.97567.h5"
model = tf.keras.models.load_model(model)
model.summary()


main_dir= "/home/aayush/Downloads/agent_test_data/fake/"

imgs_dir = glob.glob(main_dir+"/*")

exp_dir = "/home/aayush/Documents/liveness/models/Dkyc/Server/Customer/vamshi/exp/"
output_file = open(exp_dir+'New_puru_Agent_fake_0.97567.csv', 'w', newline='')
row = ['image_name', 'pred_score']
csv_writer  = csv.writer(output_file)
csv_writer.writerow(row)

count = 0
"""
,
a==main type is t will { make some changes in my slef nad not in the main sream @ 0.55454aavbset into them 
{
}

"""
for image_path in imgs_dir[:]:
    
    dir_name = os.path.basename(os.path.dirname(image_path))
    filename = path_leaf(image_path)
    
    preproc_image = preprocessing_img(image_path)
    model_pred = model.predict(preproc_image)
    count += 1
    if count % 100 == 0:
        print("completed >>>> ", count)
        
    row = [filename, model_pred[0][0]]
    csv_writer.writerow(row)
        
output_file.close()
