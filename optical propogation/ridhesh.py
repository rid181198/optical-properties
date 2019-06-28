#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:20:12 2019

@author: vaibhav
"""



import os
import pandas as pd
import numpy as np

def extract_params_get_ABCD(lensdata_filename=os.path.abspath("lens_train1.csv"), \
    starting_surface=1, ending_surface=None):
    
    df=pd.read_csv(lensdata_filename)
    df = df.replace(np.nan, '', regex=True)
    #############################################
    #Currently using standard surfaces
    #Later other surface types to be included
    #############################################
    df=df[df['Type']=="STANDARD"]
    num_surfaces=len(df)
    surface_number_zemax_file=np.array(df['#'], dtype='int')
    type_of_surface=list(df['Type'])
    radius_of_curvature=1e-3/(np.array(df['Curvature'])+1e-15)
    glass_name=list(df['Glass'])
    #refractive_index=get_refractive_index(glass_name)
    distance=np.array(df['Thickness'], dtype='float')*1e-3  #Factor for mm to m conversion
    semi_diameter=np.array(df['Semi-Diameter'], dtype='float')*1e-3
    conic=np.array(df['Conic'], dtype='float')
    param0=np.array(df['Parameter 0'], dtype='float')
    param1=np.array(df['Parameter 1'], dtype='float')
    param2=np.array(df['Parameter 2'], dtype='float')
    param3=np.array(df['Parameter 3'], dtype='float')
    
 
extract_params_get_ABCD(lensdata_filename=os.path.abspath("lens_train1.csv"), \
    starting_surface=1, ending_surface=None)

#for parexial rays
#defining pupilsource size and dividing into equal parts
range_pupil_max = float(input("Please enter the maximum range of the pupil in positive y direction in mm:  "))
range_pupil_min = float(input("Please enter the minimum range of the pupil in negative y direction in mm:  "))
equal_divide_pupil = float((range_pupil_max - range_pupil_min)/10)
frag_pupil_list=[]
frag_pupil_list.append(range_pupil_min)
for i in range(10):
    x = range_pupil_min + equal_divide_pupil
    frag_pupil_list.append(x)
    

#defining sag for spherical surfaces 
#h=height, R=radius of lens or inverse of curvature
R = float(input("Enter the radius of the spherical lens : "))
h = frag_pupil_list[3]
sag_sphere =  float( (h*h)/(R + ((R*R) - (h*h))**(1/2)) )

initial_object_dist = input("Enter the z-axis distance from vertex of lens to pupil :  ")


