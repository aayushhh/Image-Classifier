#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:47:43 2020

@author: Aayush
"""


import os, cv2, shutil

for path, subdirs, files in os.walk("../production_data/"):
    for file_name in files[:]:
        
        full_img_path = os.path.join(path, file_name)
        
        image = cv2.imread(full_img_path)
        try:
            height, width = image.shape[:2]
        except:
            print(full_img_path)
            continue
        
        if height == 224 and width == 224 and os.path.basename(os.path.dirname(full_img_path)) == file_name.split("_")[0]:
            
            shutil.move(full_img_path, path + "/../" + file_name)
            shutil.rmtree(path)
            
        

            
        
        
