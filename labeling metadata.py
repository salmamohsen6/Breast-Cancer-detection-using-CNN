# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:54:00 2020

@author: HP.SXO7
"""


import numpy as np
import pandas as pd
import os
import re
import shutil
from openpyxl import load_workbook
import csv
import openpyxl

#Labels for train and test data for both calc and mass cases

## Train data labels
calc_train = pd.read_csv("Calc-Training.csv")
calc_train['image_name'] = calc_train.patient_id + '_' + calc_train['left or right breast'] + '_' + calc_train['image view'] 
calc_train.drop(["image file path","cropped image file path","ROI mask file path"], axis=1, inplace=True)
calc_train.columns = ["Patient_ID","Breast_Density","Side_L_R","Image View","Abnormality_ID","Abnormality_Type","Mass_Shape","Mass_Margins","Assessment","Pathology", "Subtlety","Image_Name"]

mass_train = pd.read_csv("Mass-Training.csv")
mass_train['image_name'] = mass_train.patient_id + '_' + mass_train['left or right breast'] + '_' + mass_train['image view'] 
mass_train.drop(["image file path","cropped image file path","ROI mask file path"], axis=1, inplace=True)
mass_train.columns = ["Patient_ID","Breast_Density","Side_L_R","Image View","Abnormality_ID","Abnormality_Type","Mass_Shape","Mass_Margins","Assessment","Pathology", "Subtlety","Image_Name"]


# Train and Test label
train_label = pd.concat([calc_train, mass_train], axis = 0)
train_label['Pathology'][train_label['Pathology'] == 'BENIGN_WITHOUT_CALLBACK'] = 'BENIGN'
train_label['Class'] = train_label['Pathology'] + '_' + train_label['Abnormality_Type']

 #Set image_name to be the index
train_label.set_index("Image_Name", inplace = True)


calc_train.head()
mass_train.head()



train_label

writer = pd.ExcelWriter('output5555.xlsx')
# write dataframe to excel
train_label.to_excel(writer)
# save the excel
writer.save()
