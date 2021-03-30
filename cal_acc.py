#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:01:27 2021

@author: Aayush
"""

import pandas as pd
import glob, os, shutil, ntpath



def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def createDir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

csvs_list = "/home/aayush/Documents/liveness/face_liveness-ISSUES-1614273101161.csv"
df =pd.read_csv(csvs_list)
print(csvs_list)
thresh_list = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
# thresh_val = 0.5
missed_fake = []
    
for thresh in thresh_list:
    '''
    0- customer, 1-agent
    '''
#customer fake
    # df_1 = df.groupby(['type']).get_group(0)
    # df_1 = df.groupby(['fakeface']).get_group(True)
    
   
    # fake_pred = df_1[(df_1["fiopmean"] < thresh) | (df_1["fiopmean_agg"] < thresh)]
    # fake_acc = len(fake_pred) / len(df.groupby("fakeface").get_group(True))
    # print("fake acc with thresh {} : {} / {} = {}\n".format(thresh, len(fake_pred), len(df.groupby("fakeface").get_group(True)),
    #                                                                           fake_acc))
    
# #Agent Fake
    # df_1 = df.groupby(['type']).get_group(1)
    # df_1 = df.groupby(['fakeface']).get_group(True)
    # fake_pred = df_1[(df_1["fiopmean"] < thresh) ]
    # fake_acc = len(fake_pred) / len(df.groupby("fakeface").get_group(True))
    # print("fake acc with thresh {} : {} / {} = {}\n".format(thresh, len(fake_pred), len(df.groupby("fakeface").get_group(True)),
    #                                                                           fake_acc))
    
#Real Customer    
    df=df.groupby(['type']).get_group(0)
    real_pred = df[(df["fiopmean"] > thresh) & (df["fiopmean_agg"] > thresh) & (df["fakeface"] == False)]
    real_acc = len(real_pred) / len(df.groupby("fakeface").get_group(False))
    print("real acc with thresh {} : {} / {} = {}\n".format(thresh, len(real_pred), len(df.groupby("fakeface").get_group(False)),
                                                                               real_acc))

#Agnet Real
    # df=df.groupby(['type']).get_group(1)
    # real_pred = df[(df["fiopmean"] > thresh) & (df["fakeface"] == False)]
    # real_acc = len(real_pred) / len(df.groupby("fakeface").get_group(False))
    # print("real acc with thresh {} : {} / {} = {}\n".format(thresh, len(real_pred), len(df.groupby("fakeface").get_group(False)),
    #                                                                            real_acc))
