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
import matplotlib.pyplot as plt




glass_name = input("\nEnter the name of glass type :  ")
wavelength = float(input("\nEnter the wavelength in nm : "))
T =float(input("\nEnter the temeperature of surrounding in celcius : "))
P=float(input("\nEnter the pressure of surrounding in Pa : "))



#pupil define
range_pupil_max = float(input("Enter the maximum value of pupil in mm  : "))
range_pupil_min = float(input("Enter the minimum value of pupil in mm  : "))
equal_divide_pupil = float((range_pupil_max - range_pupil_min)/10)
frag_pupil_list=[]
frag_pupil_list.append(range_pupil_min)
x = range_pupil_min
for i in range(10):
    x = x + equal_divide_pupil
    frag_pupil_list.append(x)






def sag_convex(h,R,semi_diameter):
    sag = float( ((h*h)/(R + ((R*R) - (h*h))**(1/2))) )
    return sag
def sag_concave(h,R,semi_diameter):
    sag_max = sag_convex(h,R,semi_diameter)
    sag = sag_max - float( ((h*h)/(R + ((R*R) - (h*h))**(1/2))) )
    return sag






def air_vertex(angle,initial_object_dist,i):
    air_vertex.angle = angle
    
    n_m.thermal_describtion_glass(glass_name,wavelength,P,T)
    air_vertex.n_air = n_m.thermal_describtion_glass.n_air_catT
    air_vertex.n_medium = n_m.thermal_describtion_glass.n_rel_givenT
 
    air_vertex.h = frag_pupil_list[i]
    
    
    #height at the plane passing through vertex
    if air_vertex.angle != 0 :
        air_vertex.h = air_vertex.h + ((m.tan(air_vertex.angle*m.pi/180)) * (initial_object_dist ))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
        
    #distance 
    OP = air_vertex.n_air*(initial_object_dist)/(m.cos(air_vertex.angle*m.pi/180))
    OP_r = air_vertex.n_air * (initial_object_dist)    
    air_vertex.OPD = OP - OP_r
    
    
    print("\n Initial height is ",end = ' ')
    print(air_vertex.h)
    print("\n Initial incident angle is ",end=' ')
    print(air_vertex.angle)






def convex_air_medium(R,semi_diameter):
    n_m.thermal_describtion_glass(glass_name,wavelength,P,T)
    n_medium = n_m.thermal_describtion_glass.n_rel_givenT
    n_air = air_vertex.n_air
    
    R = R
    semi_diameter = semi_diameter
    
    #height at the surface
    if air_vertex.angle != 0 :
        x = Symbol('x')
        sol = solve((air_vertex.h + (m.tan(air_vertex.angle*m.pi/180)) * (( (x*x)/(R + ((R*R) - (x*x))**(1/2)) )) - x) ,x)
        air_vertex.h = float(re(sol[0]))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
    
    
    
    #distance
    OP1 = n_air*(sag_convex(air_vertex.h,R,semi_diameter))/(m.cos(air_vertex.angle*m.pi/180))
    OP1_r = n_air*(sag_convex(air_vertex.h,R,semi_diameter))
    OPD1 = OP1 - OP1_r
    
    
    
    #angles at surface
    if air_vertex.h>0:
        angle_r_1 = (m.asin( air_vertex.h/R ))*180/m.pi
        t_angle = angle_r_1 + air_vertex.angle
        air_vertex.angle = ((m.asin( (n_air*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi - angle_r_1)
    if air_vertex.h == 0:
        angle_r_1 = (m.asin( air_vertex.h/R ))*180/m.pi
        t_angle = angle_r_1 + air_vertex.angle
        air_vertex.angle = ((m.asin( (n_air*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi - angle_r_1)  
    if air_vertex.h<0:
         angle_r_1 = float(m.asin(-air_vertex.h/R ) )*180/m.pi
         t_angle = float(angle_r_1 - air_vertex.angle)
         air_vertex.angle = (angle_r_1  -  float(m.asin( (n_air*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi  )

    
    #distance
    sag_max = sag_convex(semi_diameter,R,semi_diameter)
    sag = sag_convex(air_vertex.h,R,semi_diameter)
    OP2 = n_medium*(sag_max - sag)/m.cos(air_vertex.angle*m.pi/180)
    OP2_r = n_medium*(sag_max - sag)
    OPD2 = (OP2 - OP2_r)
    convex_air_medium.OPD = OPD1+OPD2
    
    
    #Final height
    sag_max = sag_convex(semi_diameter,R,semi_diameter)
    sag = sag_convex(air_vertex.h,R,semi_diameter)
    if air_vertex.angle != 0 :
        air_vertex.h = air_vertex.h + ((m.tan(air_vertex.angle*m.pi/180)) * (sag_max - sag))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
    
    
    print("\n Final height at end of the lens is :  ",end=' ' )
    print(air_vertex.h)
    print("\n Angle at surface is  : ",end=' ')
    print(air_vertex.angle)
    




def convex_medium_air(R,semi_diameter):
    
    n_m.thermal_describtion_glass(glass_name,wavelength,P,T)
    n_medium = n_m.thermal_describtion_glass.n_rel_givenT
    n_air = air_vertex.n_air
    
    R = R
    semi_diameter = semi_diameter
    #height at the surface
    if air_vertex.angle != 0 :
        x = Symbol('x')
        sol = solve((air_vertex.h + (m.tan(air_vertex.angle*m.pi/180)) * (( (x*x)/(R + ((R*R) - (x*x))**(1/2)) )) - x) ,x)
        air_vertex.h = float(re(sol[0]))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
    
    
    
    #distance
    OP1 = n_medium*(sag_convex(air_vertex.h,R,semi_diameter))/(m.cos(air_vertex.angle*m.pi/180))
    OP1_r = n_medium*(sag_convex(air_vertex.h,R,semi_diameter))
    OPD1 = OP1 - OP1_r
    
    
    
    #angles at surface
    if air_vertex.h>0:
        angle_r_1 = (m.asin( air_vertex.h/R ))*180/m.pi
        t_angle = angle_r_1 + air_vertex.angle
        air_vertex.angle = ((m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_air) ))*180/m.pi - angle_r_1)
    if air_vertex.h == 0:
        angle_r_1 = (m.asin( air_vertex.h/R ))*180/m.pi
        t_angle = angle_r_1 + air_vertex.angle
        air_vertex.angle = ((m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_air) ))*180/m.pi - angle_r_1)  
    if air_vertex.h<0:
         angle_r_1 = float(m.asin(-air_vertex.h/R ) )*180/m.pi
         t_angle = float(angle_r_1 - air_vertex.angle)
         air_vertex.angle = (angle_r_1  -  float(m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_air) ))*180/m.pi  )

     
    #distance
    sag_max = sag_convex(semi_diameter,R,semi_diameter)
    sag = sag_convex(air_vertex.h,R,semi_diameter)
    OP2 = n_air*(sag_max - sag)/m.cos(air_vertex.angle*m.pi/180)
    OP2_r = n_air*(sag_max - sag)
    OPD2 = OP2 - OP2_r
    convex_medium_air.OPD = OPD1+OPD2
    
    
    #Final height
    sag_max = sag_convex(semi_diameter,R,semi_diameter)
    sag = sag_convex(air_vertex.h,R,semi_diameter)
    if air_vertex.angle != 0 :
        air_vertex.h = air_vertex.h + ((m.tan(air_vertex.angle*m.pi/180)) * (sag_max - sag))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
        
   
    
    print("\n Final height at end of the lens is :  ",end=' ' )
    print(air_vertex.h)
    print("\n Angle at surface is  : ",end=' ')
    print(air_vertex.angle)






def convex_medium_medium(R,semi_diameter):
    
    n_m.thermal_describtion_glass(glass_name,wavelength,P,T)
    n_medium = n_m.thermal_describtion_glass.n_rel_givenT
    
    R = R
    semi_diameter = semi_diameter
    #height at the surface
    if air_vertex.angle != 0 :
        x = Symbol('x')
        sol = solve((air_vertex.h + (m.tan(air_vertex.angle*m.pi/180)) * (( (x*x)/(R + ((R*R) - (x*x))**(1/2)) )) - x) ,x)
        air_vertex.h = float(re(sol[0]))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
    
    
    
    #distance
    OP1 = n_medium*(sag_convex(air_vertex.h,R,semi_diameter))/(m.cos(air_vertex.angle*m.pi/180))
    OP1_r = n_medium*(sag_convex(air_vertex.h,R,semi_diameter))
    OPD1 = OP1 - OP1_r
    
    
    
    #angles at surface
    if air_vertex.h>0:
        angle_r_1 = (m.asin( air_vertex.h/R ))*180/m.pi
        t_angle = angle_r_1 + air_vertex.angle
        air_vertex.angle = ((m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi - angle_r_1)
    if air_vertex.h == 0:
        angle_r_1 = (m.asin( air_vertex.h/R ))*180/m.pi
        t_angle = angle_r_1 + air_vertex.angle
        air_vertex.angle = ((m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi - angle_r_1)  
    if air_vertex.h<0:
         angle_r_1 = float(m.asin(-air_vertex.h/R ) )*180/m.pi
         t_angle = float(angle_r_1 - air_vertex.angle)
         air_vertex.angle = (angle_r_1  -  float(m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi  )

     
    #distance
    sag_max = sag_convex(semi_diameter,R,semi_diameter)
    sag = sag_convex(air_vertex.h,R,semi_diameter)
    OP2 = n_medium*(sag_max - sag)/m.cos(air_vertex.angle*m.pi/180)
    OP2_r = n_medium*(sag_max - sag)
    OPD2 = OP2 - OP2_r
    convex_medium_medium.OPD = OPD1+OPD2
    
    
    #Final height
    sag_max = sag_convex(semi_diameter,R,semi_diameter)
    sag = sag_convex(air_vertex.h,R,semi_diameter)
    if air_vertex.angle != 0 :
        air_vertex.h = air_vertex.h + ((m.tan(air_vertex.angle*m.pi/180)) * (sag_max - sag))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
        
   
    
    print("\n Final height at end of the lens is :  ",end=' ' )
    print(air_vertex.h)
    print("\n Angle at surface is  : ",end=' ')
    print(air_vertex.angle)





def concave_air_medium(R,semi_diameter):
    
    n_m.thermal_describtion_glass(glass_name,wavelength,P,T)
    n_medium = n_m.thermal_describtion_glass.n_rel_givenT
    n_air = air_vertex.n_air
    
    R = R
    semi_diameter = semi_diameter
    sag_max = sag_convex(semi_diameter,R,semi_diameter)
    
    #height at the surface
    if air_vertex.angle != 0 :
        x = Symbol('x')
        sol = solve((air_vertex.h + (m.tan(air_vertex.angle*m.pi/180)) * (( sag_max - (x*x)/(R + ((R*R) - (x*x))**(1/2)) )) - x) ,x)
        air_vertex.h = float(re(sol[0]))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
    
    
    
    #distance
    OP1 = n_air*(sag_max - sag_convex(air_vertex.h,R,semi_diameter))/(m.cos(air_vertex.angle*m.pi/180))
    OP1_r = n_air*(sag_max - sag_convex(air_vertex.h,R,semi_diameter))
    OPD1 = OP1 - OP1_r
    
     
    
    
    #angles at surface
    if air_vertex.h>0:
        angle_r_1 = (m.asin( air_vertex.h/R ))*180/m.pi
        t_angle = angle_r_1 - air_vertex.angle
        air_vertex.angle = (-(m.asin( (n_air*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi + angle_r_1)
    if air_vertex.h == 0:
        angle_r_1 = (m.asin( air_vertex.h/R ))*180/m.pi
        t_angle = angle_r_1 - air_vertex.angle
        air_vertex.angle = (-(m.asin( (n_air*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi + angle_r_1)  
    if air_vertex.h<0:
         angle_r_1 = float(m.asin(-air_vertex.h/R ) )*180/m.pi
         t_angle = float(angle_r_1 + air_vertex.angle)
         air_vertex.angle = (-angle_r_1  +  float(m.asin( (n_air*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi  )

   
    #distance
    sag = sag_convex(air_vertex.h,R,semi_diameter)
    OP2 = n_medium*(sag)/m.cos(air_vertex.angle*m.pi/180)
    OP2_r = n_medium*(sag)
    OPD2 = OP2 - OP2_r
    concave_air_medium.OPD = OPD1+OPD2
    
    #Final height
    sag = sag_convex(air_vertex.h,R,semi_diameter)
    if air_vertex.angle != 0 :
        air_vertex.h = air_vertex.h + ((m.tan(air_vertex.angle*m.pi/180)) * ( sag))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
        
    
    
    
    
    print("\n Final height at end of the lens is :  ",end=' ' )
    print(air_vertex.h)
    print("\n Angle at surface is  : ",end=' ')
    print(air_vertex.angle)
    





def concave_medium_air(R,semi_diameter):
    n_m.thermal_describtion_glass(glass_name,wavelength,P,T)
    n_medium = n_m.thermal_describtion_glass.n_rel_givenT
    n_air = air_vertex.n_air
    
    R = R
    semi_diameter = semi_diameter
    sag_max = sag_convex(semi_diameter,R,semi_diameter)
    
    #height at the surface
    if air_vertex.angle != 0 :
        x = Symbol('x')
        sol = solve((air_vertex.h + (m.tan(air_vertex.angle*m.pi/180)) * (( sag_max - (x*x)/(R + ((R*R) - (x*x))**(1/2)) )) - x) ,x)
        air_vertex.h = float(re(sol[0]))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
    
    
    
    #distance
    OP1 = n_medium*(sag_max - sag_convex(air_vertex.h,R,semi_diameter))/(m.cos(air_vertex.angle*m.pi/180))
    OP1_r = n_medium*(sag_max - sag_convex(air_vertex.h,R,semi_diameter))
    OPD1 =( OP1 - OP1_r)
    
    
    
    #angles at surface
    if air_vertex.h>0:
        angle_r_1 = (m.asin( air_vertex.h/R ))*180/m.pi
        t_angle = angle_r_1 - air_vertex.angle
        air_vertex.angle = (-(m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_air) ))*180/m.pi + angle_r_1)
    if air_vertex.h == 0:
        angle_r_1 = (m.asin( air_vertex.h/R ))*180/m.pi
        t_angle = angle_r_1 - air_vertex.angle
        air_vertex.angle = (-(m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_air) ))*180/m.pi + angle_r_1)  
    if air_vertex.h<0:
         angle_r_1 = float(m.asin(-air_vertex.h/R ) )*180/m.pi
         t_angle = float(angle_r_1 + air_vertex.angle)
         air_vertex.angle = (-angle_r_1  +  float(m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_air) ))*180/m.pi  )

     
    #distance
    sag = sag_convex(air_vertex.h,R,semi_diameter)
    OP2 = n_air*(sag)/m.cos(air_vertex.angle*m.pi/180)
    OP2_r = n_air*(sag)
    OPD2 = OP2 - OP2_r
    concave_medium_air.OPD = OPD1+OPD2
    
    
    #Final height
    sag = sag_convex(air_vertex.h,R,semi_diameter)
    if air_vertex.angle != 0 :
        air_vertex.h = air_vertex.h + ((m.tan(air_vertex.angle*m.pi/180)) * ( sag))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
        
   
    
    print("\n Final height at end of the lens is :  ",end=' ' )
    print(air_vertex.h)
    print("\n Angle at surface is  : ",end=' ')
    print(air_vertex.angle)
    
   
    
    
    
def concave_medium_medium(R,semi_diameter):
    n_m.thermal_describtion_glass(glass_name,wavelength,P,T)
    n_medium = n_m.thermal_describtion_glass.n_rel_givenT
    
    R = R
    semi_diameter = semi_diameter
    sag_max = sag_convex(semi_diameter,R,semi_diameter)
    
    #height at the surface
    if air_vertex.angle != 0 :
        x = Symbol('x')
        sol = solve((air_vertex.h + (m.tan(air_vertex.angle*m.pi/180)) * (( sag_max - (x*x)/(R + ((R*R) - (x*x))**(1/2)) )) - x) ,x)
        air_vertex.h = float(re(sol[0]))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
    
    
    
    #distance
    OP1 = n_medium*(sag_max - sag_convex(air_vertex.h,R,semi_diameter))/(m.cos(air_vertex.angle*m.pi/180))
    OP1_r = n_medium*(sag_max - sag_convex(air_vertex.h,R,semi_diameter))
    OPD1 =( OP1 - OP1_r)
    
    
    
    #angles at surface
    if air_vertex.h>0:
        angle_r_1 = (m.asin( air_vertex.h/R ))*180/m.pi
        t_angle = angle_r_1 - air_vertex.angle
        air_vertex.angle = (-(m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi + angle_r_1)
    if air_vertex.h == 0:
        angle_r_1 = (m.asin( air_vertex.h/R ))*180/m.pi
        t_angle = angle_r_1 - air_vertex.angle
        air_vertex.angle = (-(m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi + angle_r_1)  
    if air_vertex.h<0:
         angle_r_1 = float(m.asin(-air_vertex.h/R ) )*180/m.pi
         t_angle = float(angle_r_1 + air_vertex.angle)
         air_vertex.angle = (-angle_r_1  +  float(m.asin( (n_medium*(m.sin(t_angle*m.pi/180))/n_medium) ))*180/m.pi  )

     
    #distance
    sag = sag_convex(air_vertex.h,R,semi_diameter)
    OP2 = n_medium*(sag)/m.cos(air_vertex.angle*m.pi/180)
    OP2_r = n_medium*(sag)
    OPD2 = OP2 - OP2_r
    concave_medium_medium.OPD = OPD1+OPD2
    
    
    #Final height
    sag = sag_convex(air_vertex.h,R,semi_diameter)
    if air_vertex.angle != 0 :
        air_vertex.h = air_vertex.h + ((m.tan(air_vertex.angle*m.pi/180)) * ( sag))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
        
   
    
    print("\n Final height at end of the lens is :  ",end=' ' )
    print(air_vertex.h)
    print("\n Angle at surface is  : ",end=' ')
    print(air_vertex.angle)
    
    
    
    
    
    
    
def iblock_air(length):
    length = length
    #height = float(input("Enter the height of the block : "))
    
    if air_vertex.angle != 0 :
        air_vertex.h = air_vertex.h + ((m.tan(air_vertex.angle*m.pi/180)) * (length))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
    
    #distance 
    OP = air_vertex.n_air*(length)/(m.cos(air_vertex.angle*m.pi/180))
    OP_r = air_vertex.n_air * (length)    
    iblock_air.OPD = OP - OP_r
    
    
    print("\n Final height is :  ",end= ' ')
    print(air_vertex.h)
    
 
    
    
    
def iblock_medium(length):
    length = length
    #height = float(input("Enter the height of the block : "))
    
    if air_vertex.angle != 0 :
        air_vertex.h = air_vertex.h + ((m.tan(air_vertex.angle*m.pi/180)) * (length))
    if air_vertex.angle == 0:
        air_vertex.h =float(air_vertex.h)
    
    #distance 
    OP = air_vertex.n_medium*(length)/(m.cos(air_vertex.angle*m.pi/180))
    OP_r = air_vertex.n_medium * (length)    
    iblock_medium.OPD = OP - OP_r
    
    
    print("\n Final height is :  ",end= ' ')
    print(air_vertex.h)





def refraction_air_medium_plane():
    n_air = air_vertex.n_air
    n_medium = air_vertex.n_medium
    
    #snell's law
    if air_vertex.angle != 0 :
        air_vertex.angle = (m.asin(n_air*(m.sin(air_vertex.angle*m.pi/180))/n_medium))*180/m.pi
    if air_vertex.angle == 0 :
        air_vertex.angle = air_vertex.angle
        
    print("\n Angle after refraction is :  ",end=' ')
    print(air_vertex.angle)
  



      
def refraction_medium_air_plane():
    n_air = air_vertex.n_air
    n_medium = air_vertex.n_medium
    
    #snell's law
    if air_vertex.angle != 0 :
        air_vertex.angle = (m.asin(n_medium*(m.sin(air_vertex.angle*m.pi/180))/n_air))*180/m.pi
    if air_vertex.angle == 0 :
        air_vertex.angle = air_vertex.angle
        
        
    print("\n Angle after refraction is :  ",end=' ')
    print(air_vertex.angle)
        








if __name__ == "__main__" :

    final_h = []
    OPD_list =[]
    for i in range(len(frag_pupil_list)):
    
        #air_vertex(0.0,10,i)
        #OPD1 = air_vertex.OPD
        
        #convex_air_medium(28.7356,12.5)
        #OPD2 =convex_air_medium.OPD
        
        #iblock_medium(0.9911)
        #OPD3 = iblock_medium.OPD
        
        #concave_medium_medium(21.3675,12.5)
        #OPD4 = concave_medium_medium.OPD
        
        #iblock_medium(2.8839)
        #OPD5 = iblock_medium.OPD
        
        #concave_medium_air(82.6446,4.38)
        #OPD6 = concave_medium_air.OPD
        
        #iblock_air(37.0)
        #OPD7 = iblock_air.OPD
        
        
        
        air_vertex(0.0,10,i)
        OPD8 = air_vertex.OPD
        
        
        
        
        convex_air_medium(82.6446,4.45)
        OPD9 = convex_air_medium.OPD
        
        iblock_medium(2.8801)
        OPD10 = iblock_medium.OPD
        
        convex_medium_medium(21.3675,12.5)
        OPD11 = convex_medium_medium.OPD
        
        iblock_medium(0.9911)
        OPD12 = iblock_medium.OPD
        
        concave_medium_air(28.7356,12.5)
        OPD13 = concave_medium_air.OPD
        
        iblock_air(37.0)
        OPD14 = iblock_air.OPD
        
        final_h.append(air_vertex.h)
        OPD = (OPD8 +OPD9+ OPD10+ OPD11+ OPD12+ OPD13+ OPD14)
        OPD_list.append(OPD)
        
        
    
    
    
    
    #plots
    plt.figure(figsize=(10,10))
    plt.plot(final_h,frag_pupil_list,'r-')
    plt.xlabel("final height in mm")
    plt.ylabel("initial height from optical axis in mm")
    plt.show()
    
    
    plt.figure(figsize=(10,10))
    plt.plot(OPD_list,frag_pupil_list,'r-')
    plt.xlabel("OPD in mm")
    plt.ylabel("initial height from optical axis in mm")
    plt.show()
    
            
            
        
    
    









