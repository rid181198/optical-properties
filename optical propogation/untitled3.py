# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:51:55 2019

@author: crystal
"""
from sympy.solvers import solve
from sympy import Symbol
from sympy.functions import re
import math as m
import get_refractive_index_temperature as n_m
def surface_convex(angle,frag_pupil_list,initial_object_dist,R,glass,wavelength,pressure,temperature):
    n_m.thermal_describtion_glass(glass,wavelength,pressure,temperature)

    n_air =float(input("enter the air refractive index from above list "))
    n_medium =float(input("enter the medium refractive index from above list "))
    h = frag_pupil_list[1]
    #height at surface1
    if angle != 0 :
        x= Symbol('x')
        sol = solve( (h + ((m.tan(angle*m.pi/180)) * (initial_object_dist +  ((x*x)/(R + ((R*R) - (x*x))**(1/2)) ) )) - x), x)
        h_1 = float(re(sol[0]))
    if angle == 0:
        h_1 =float(h) 
         
    #angles at surface1
   
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
    
def surface_concave(h,thickness,image_dist,angle,frag_pupil_list,initial_object_dist,R,glass,wavelength,pressure,temperature):
    n_m.thermal_describtion_glass(glass,wavelength,pressure,temperature)

    n_air =float(input("enter the air refractive index from above list "))
    n_medium =float(input("enter the medium refractive index from above list "))
    
    
     #height
    if angle != 0 :
        x= Symbol('x')
        sol2 = solve( (h + ((m.tan(angle*m.pi/180)) * (thickness - (float( (h*h)/(R + ((R*R) - (h*h))**(1/2)) )) - ( (x*x)/(R + ((R*R) - (x*x))**(1/2)) ) )) - x), x)
        h_1 = float(re(sol2[0]))
        
    if angle == 0:
        h_1 = h

    print("\n   Height at surface two is ",end= ' ' )
    print(h_1)
    print("\n   Angle 3 at surface two is ", end= ' ')
    print((angle)) 




    #at image plane for R =21.36 it is I = 10.68
    if h_1>0:
     
      angle_r_2 = (m.asin( h_1/R ))*180/m.pi
      t_angle = angle_r_2 - (angle)
      angle_3 = ((-(m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_air) ))*180/m.pi) + angle_r_2)
     

        
    if h_1<0:
    
       angle_r_2 = float(m.asin(-h_1/R ) )*180/m.pi
       t_angle = float(angle_r_2 + angle)
       angle_3 = (-angle_r_2 + float(m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_air) ))*180/m.pi  )

    print("\n   Height at surface two is ",end= ' ' )
    print(h_1)
    print("\n   Angle 4 at surface one is ", end= ' ')
    print(angle_3)  

def bet_lens():
    sag_sphere =  float( (h*h)/(R + ((R*R) - (h*h))**(1/2)) )
    