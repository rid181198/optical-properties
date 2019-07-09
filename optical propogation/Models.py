# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 13:25:42 2019

@author: crystal
"""
import matplotlib.pyplot as plt
import Final_aberration as fa





final_h = []
OPD_list =[]



#model1 for verification with link https://ophysics.com/l14.html
for i in range(len(fa.frag_pupil_list)):
    fa.air_vertex(0,10,i)
    OPD1 = fa.air_vertex.OPD
    
    fa.convex_air_medium(10,4.5)
    OPD2 = fa.convex_air_medium.OPD
    
    fa.concave_medium_air(10,4,5)
    OPD3 = fa.concave_medium_air.OPD
    
    fa.iblock_air(9.00)
    OPD4 = fa.iblock_air.OPD
    
    
    final_h.append(fa.air_vertex.h)
    OPD = OPD1 + OPD2 +OPD3 +OPD4
    OPD_list.append(OPD)






#plots
plt.figure(figsize=(10,10))
plt.plot(final_h,fa.frag_pupil_list,'r-')
plt.xlabel("final height in mm")
plt.ylabel("initial height from optical axis in mm") 
plt.show()
    
    
plt.figure(figsize=(10,10))
plt.plot(OPD_list,fa.frag_pupil_list,'r-')
plt.xlabel("OPD in mm")
plt.ylabel("initial height from optical axis in mm")
plt.show()
    
