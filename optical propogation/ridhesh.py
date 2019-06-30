#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:20:12 2019

@author: vaibhav
"""
import matplotlib.pyplot as plt
import math as m
from sympy.solvers import solve
from sympy import Symbol
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

#for parexial rays angle=0
angle = float(input("Enter the incident angle in radian : "))

#defining pupilsource size and dividing into equal parts
semi_diameter = float(input("Enter the semi diameter in mm : "))
range_pupil_max = float(input("Please enter the maximum range of the pupil in positive y direction in mm:  "))
range_pupil_min = float(input("Please enter the minimum range of the pupil in negative y direction in mm:  "))
equal_divide_pupil = float((range_pupil_max - range_pupil_min)/20)
frag_pupil_list=[]
frag_pupil_list.append(range_pupil_min)
x = range_pupil_min
for i in range(20):
    x = x + equal_divide_pupil
    frag_pupil_list.append(x)
    

#defining sag for spherical surfaces 
#h=height, R=radius of lens or inverse of curvature
thickness = float(input("Enter the thickness in mm : " ))
R = float(input("Enter the radius of the spherical lens : "))
image_dist = ((R)-(thickness/2))
initial_object_dist = float(input("Enter the z-axis distance from vertex of lens to pupil :  "))
OPD_list=[]
h3_list=[]
for i in range(len(frag_pupil_list)):
    h = frag_pupil_list[i]


    sag_sphere =  float( (h*h)/(R + ((R*R) - (h*h))**(1/2)) )
    sag_max = float( (semi_diameter*semi_diameter)/(R + ((R*R) - (semi_diameter*semi_diameter))**(1/2)) )





    #height at surface1
    if angle != 0 :
        x= Symbol('x')
        sol = solve( (h + ((m.tan(angle*m.pi/180)) * (initial_object_dist +  ((x*x)/(R + ((R*R) - (x*x))**(1/2)) ) )) - x), x)
        h_1 = float(sol[0])
    if angle == 0:
        h_1 =float(h) 
         
    #angles at surface1
    n_air =float(1)
    n_medium =float(1.5)
    if h_1>0:
        angle_r_1 = (m.asin( h_1/R ))*180/m.pi
        t_angle = angle_r_1 + angle
        angle_2 = ((m.asin( (n_air*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi - angle_r_1)
       
    if h_1<0:
        angle_r_1 = float(m.asin(-h_1/R ) )*180/m.pi
        t_angle = float(angle_r_1 - angle)
        angle_2 = (angle_r_1  -  float(m.asin( (n_air*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi  )
       



    print("\n   Height at surface one is ",end= ' ' )
    print(h_1)
    print("\n   Angle 1 at surface one is ", end= ' ')
    print((angle))
    
    #print(angle_r_1)   
    print("\n   Height at surface one is ",end= ' ' )
    print(h_1)
    print("\n   Angle 2 at surface one is ", end= ' ')
    print(angle_2)    



    #at surface2
    #height
    if angle_2 != 0 :
        x= Symbol('x')
        sol2 = solve( (h_1 + ((m.tan(angle_2*m.pi/180)) * (thickness - (float( (h_1*h_1)/(R + ((R*R) - (h_1*h_1))**(1/2)) )) - ( (x*x)/(R + ((R*R) - (x*x))**(1/2)) ) )) - x), x)
        h_2 = float(sol2[0])
    if angle_2 == 0:
        h_2 = h_1
    
    #if angle_2 !=0:
     ##  h_2 = float(sol2[0])
    print("\n   Height at surface two is ",end= ' ' )
    print(h_2)
    print("\n   Angle 3 at surface two is ", end= ' ')
    print((angle_2)) 




    #at image plane for R =21.36 it is I = 10.68
    if h_2>0:
     
      angle_r_2 = (m.asin( h_2/R ))*180/m.pi
      t_angle = angle_r_2 - (angle_2)
      angle_3 = ((-(m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_air) ))*180/m.pi) + angle_r_2)
     

        
    if h_2<0:
    
       angle_r_2 = float(m.asin(-h_2/R ) )*180/m.pi
       t_angle = float(angle_r_2 + angle_2)
       angle_3 = (-angle_r_2 + float(m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_air) ))*180/m.pi  )

    print("\n   Height at surface two is ",end= ' ' )
    print(h_2)
    print("\n   Angle 4 at surface one is ", end= ' ')
    print(angle_3)  

    sag_sphere_h1 =  float( (h_1*h_1)/(R + ((R*R) - (h_1*h_1))**(1/2)) )
    sag_sphere_h2 =  float( (h_2*h_2)/(R + ((R*R) - (h_2*h_2))**(1/2)) )  

    if angle_3 != 0 :
        x= Symbol('x')
        sol3 = solve( (h_2 + ((m.tan(angle_3*m.pi/180)) * (image_dist + sag_sphere_h2)) - x), x)
        h_3 = float(sol3[0])
    if angle_3 == 0:
        h_3 = h_2
    print("\n   Height at image plane would be ",end= ' ')
    print(h_3)

    print("\nInitial height for angle ",end=' ')
    print(angle)
    print('is ' ,end= ' ')
    print(h)


    OP_ref = ( (n_air*initial_object_dist)  + (n_medium*thickness) + (n_air*image_dist) )
    OP =( (n_air*((initial_object_dist + sag_sphere_h1)/(m.cos(abs(angle)*m.pi/180))))  +  (n_medium*((thickness + 0 -sag_sphere_h1 - sag_sphere_h2)/(m.cos(abs(angle_2)*m.pi/180))) ) +  (n_air*(image_dist + sag_sphere_h2)/m.cos(abs(angle_3)*m.pi/180)) )
    OPD = OP - OP_ref
    print("\nOPD is ",end= ' ')
    print(OPD)
    OPD_list.append(OPD)
    h3_list.append(h_3)
    
plt.figure(figsize=(10,10))
plt.plot(OPD_list,frag_pupil_list,'r-')
plt.xlabel("OPD in mm")
plt.ylabel("Height from optical axis in mm")
plt.show()

plt.figure(figsize=(10,10))
plt.plot(h3_list,frag_pupil_list,'r-')
plt.xlabel("final height in mm")
plt.ylabel("inital height in mm")
plt.show()

