#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 15:28:09 2020

@author: aayush
"""

import shutil
import os
import pandas as pd
import numpy as np
arr=[]

destination = "/home/aayush/Downloads/split1"
# destination2 = "//home/srikanth/Python_for_CSV/ground_truths2/"
source = "/home/aayush/Downloads/dark_fake./fake"

# files = os.listdir(source)
'''
:764  will from 1 to 764
'''
for data_file in sorted(os.listdir(source))[:5000]:
    new_path = shutil.move(f"{source}/{data_file}", destination)
    #print(new_path)
    arr.append(data_file)   
    
 #[:1000]