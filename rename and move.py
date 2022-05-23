# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:57:13 2020

@author: HP.SXO7
"""

import numpy as np
import pandas as pd
import os
import re
import shutil
from shutil import move

#Rename test Calc/Mass ROI DICOM files and move them to a single directory
def rename_and_move_files (path, origin_dir, dest_dir):
    directories = os.listdir(path + origin_dir)
    
    for directory in directories: 
        subdirs = os.listdir(path + origin_dir + "/" + directory)
        
        i = 1
        for subdir in subdirs:
            subsubdirs = os.listdir(path + origin_dir + "/" + directory + "/" + subdir)
            
            for subsubdir in subsubdirs:
                files = os.listdir(path + origin_dir + "/" + directory + "/" + subdir + "/" + subsubdir)
                
                j = 1
                for file in files:
                    
                    patient_id = str(re.findall("_(P_[\d]+)_", directory))[2:-2]
                    image_side = str(re.findall("_(LEFT|RIGHT)_", directory))[2:-2]
                    image_type = str(re.findall("(CC|MLO)", directory))[2:-2]
                 
                   
                                       
                    files_origin_path = os.listdir(path + origin_dir + "/" + directory + "/" + subdir + "/" + subsubdir + "/")
                    
                    new_name = patient_id + "_" + image_side + "_" + image_type +'.dcm'
            
                    
                    os.rename(os.path.join(path, origin_dir, directory, subdir, subsubdir, file),os.path.join(path, dest_dir, new_name))
                                        
                    i = int(i)
                    j = int(j)
                    i += 1
                    j +=1

                    
rename_and_move_files("F:/CBIS-DDSM/compressed/", origin_dir = "calc-training", dest_dir = "Calc_Training")

