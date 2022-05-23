# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:08:40 2020

@author: BioHelwan
"""

from glob import glob                                                           
import cv2 
pngs = glob('D:/Breast Cancer Grad.Proj/try/train/malignant_mass/*.png')

for j in pngs:
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + 'jpg', img)