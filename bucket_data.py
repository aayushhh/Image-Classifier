#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:39:59 2020

@author: Aayush
"""

import cv2, glob, os, ntpath, csv

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def createDir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def shift_images(img_dir):
    
    img_type = "None"
    error = []
    for img_path in img_dir:
        try:
            
            print("\npress p for paper fake")
            print("press s for Screen fake")
            print("press r for Real image")
            print("press u if Uknown\n")
            
            image = cv2.imread(img_path)
            
            cv2.imshow('frame', cv2.resize(image, (512,512)))
            key = cv2.waitKey(0)
            
            file_name = path_leaf(img_path)
    
            if key == ord("p"):   ##Paper Fake
                cv2.imwrite(new_paper_fake_dir + file_name, image)
                print("Image shifted to Paper Fake directory", file_name)
                img_type = "paper_fake"
                
            elif key == ord("s"):   ##Screen Fake
                cv2.imwrite(new_screen_fake_dir + file_name, image)
                print("Image shifted to Screen Fake directory", file_name)
                img_type = "screen_fake"
                
            elif key == ord("r"):  ## Real Image
                cv2.imwrite(new_real_dir + file_name, image)
                print("Image shifted to Real Image directory", file_name)
                img_type = "real_image"
                
            elif key == ord("u"):  ## Uknown
                cv2.imwrite(new_unknwon_dir + file_name, image)
                print("Image shifted to Unknown directory", file_name)
                img_type = "unknown_image"
                
            else:
                cv2.imwrite(new_unknwon_dir + file_name, image)
                print("Image shifted to Unknown directory", file_name)
                img_type = "unknown_image"
                
            
            row = [file_name.split('_')[0], img_type]
            csv_writer.writerow(row)
        except:
            error.append(img_path)
            continue
            
        
    print("error images: ", error)
    cv2.destroyAllWindows()    
    print("finished : {} dir".format(dir_date))
    
    

main_dir = "../production_data/nov_week3/"
dir_date = "22_nov/customer/"

new_real_dir = main_dir + dir_date + "images/real/"
new_paper_fake_dir = main_dir + dir_date + "images/fake/paper/"
new_screen_fake_dir = main_dir + dir_date + "images/fake/screen/"
new_unknwon_dir = main_dir + dir_date + "images/unknown/"

createDir(new_real_dir)
createDir(new_paper_fake_dir)
createDir(new_screen_fake_dir)
createDir(new_unknwon_dir)


real_images = glob.glob(main_dir + dir_date + "/fn/*")[:]
fake_images = glob.glob(main_dir + dir_date + "/fp/*")[:]


output_file = open(main_dir + dir_date + 'dir_names.csv', 'a', newline='')
row = ['xcall_id', 'img_type']
csv_writer  = csv.writer(output_file)
csv_writer.writerow(row)

shift_images(real_images)
shift_images(fake_images)

output_file.close()
    














