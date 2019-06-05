# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:00:25 2019

@author: crystal
"""
import os
import numpy as np
import matplotlib.pyplot as plt






#query function
def name_formula(abbe_name_formula,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000
           
            print("\nRefractive index is  ")
            print(abbe_name_formula(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)) 
        else:
            break 
        
        






#defining function or data set for each formula
def describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
     #details of glass    
     print('\nGlass dispersion formula number is ' + formula_number)
     print("\nConstants values for  are, \n\nA0 : " , end='')
     print(A0)
     print('\nA1 : ',end='' )
     print(A1)
     print('\nA2 : ',end='' )
     print(A2)
     print('\nA3 : ',end='' )
     print(A3)
     print('\nA4 : ',end='' )
     print(A4)
     print('\nA5 : ',end='' )
     print(A5)
     print('\nA6 : ',end='' )
     print(A6)
     print('\nA7 : ',end = '' )
     print(A7)
     print('\nA8 : ',end = '' )
     print(A8)
     print('\nA9 : ' ,end='')
     print(A9)
    







def plot(n,wavelength,glass_name,formula_number):
     plot_name = str(glass_name +'_'+ str(formula_number))
     wavelength_nanometer=wavelength*1000
     plt.plot(wavelength_nanometer,n,'r-')
     plt.xlabel('Wavelength \u03BB (nm) ' , fontsize= 14)
     plt.ylabel('Refractive Index n ' , fontsize = 14 )
     plt.savefig(os.path.abspath('Plots\\'+'RI_Wavlength_'+plot_name+'.png'))
     plt.show()
     








#abbe number
def abbe_schott(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    return n       
#formulas for all dispersion 
def schott(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    plot(n,wavelength,glass_name,formula_number)
    
    #abbe number
    #def abbe_schott(wavelength):
        #n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
        #return n  
    
    abbe_number = (abbe_schott(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_schott(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_schott(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  " )
    print(abbe_number) 
  
    #calling function for query function
    name_formula(abbe_schott,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9) 
    

    






#abbe number
def abbe_sellmeier1(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = np.sqrt(1.0000000000 + (A0*(wavelength*wavelength)/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3)) + (A4*wavelength*wavelength/(wavelength*wavelength - A5)))
    return n
def sellmeier1(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = np.sqrt(1.0000000000 + (A0*(wavelength*wavelength)/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3)) + (A4*wavelength*wavelength/(wavelength*wavelength - A5)))  
    plot(n,wavelength,glass_name,formula_number)
    
    #abbe number
    #def abbe_sellmeier1(wavelength):
        #n = np.sqrt(1.0000000000 + (A0*(wavelength*wavelength)/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3)) + (A4*wavelength*wavelength/(wavelength*wavelength - A5)))
        #return n
    
    abbe_number = (abbe_sellmeier1(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_sellmeier1(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_sellmeier1(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  ")
    print(abbe_number)

    #calling function for query function
    name_formula(abbe_sellmeier1,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9) 
        








#abbe number
def abbe_sellmeier2(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = (1.0000000 + A0 + A1*(wavelength*wavelength)/((wavelength*wavelength)-(A2*A2)) + A3/((wavelength*wavelength)-(A4*A4)))**(1/2)
    return n
def sellmeier2(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = (1.0000000 + A0 + A1*(wavelength*wavelength)/((wavelength*wavelength)-(A2*A2)) + A3/((wavelength*wavelength)-(A4*A4)))**(1/2)
    plot(n,wavelength,glass_name,formula_number)

    #abbe number
    #def abbe_sellmeier2(wavelength):
        #n = (1.0000000 + A0 + A1*(wavelength*wavelength)/((wavelength*wavelength)-(A2*A2)) + A3/((wavelength*wavelength)-(A4*A4)))**(1/2)
        #return n
        
    abbe_number = (abbe_sellmeier2(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_sellmeier2(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_sellmeier2(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  ")
    print(abbe_number)
    
    #calling function for query function
    name_formula(abbe_sellmeier2,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
    







#abbe number
def abbe_sellmeier3(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = (1.0000000000 + (A0*(wavelength*wavelength)/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3)) + (A4*wavelength*wavelength/(wavelength*wavelength - A5)) + (A6*wavelength*wavelength/(wavelength*wavelength - A7)))**(1/2)
    return n
def sellmeier3(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = (1.0000000000 + (A0*(wavelength*wavelength)/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3)) + (A4*wavelength*wavelength/(wavelength*wavelength - A5)) + (A6*wavelength*wavelength/(wavelength*wavelength - A7)))**(1/2)  
    plot(n,wavelength,glass_name,formula_number)

    #abbe number
    #def abbe_sellmeier3(wavelength):
        #n = (1.0000000000 + (A0*(wavelength*wavelength)/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3)) + (A4*wavelength*wavelength/(wavelength*wavelength - A5)) + (A6*wavelength*wavelength/(wavelength*wavelength - A7)))**(1/2)
        #return n
        
    abbe_number = (abbe_sellmeier3(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_sellmeier3(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_sellmeier3(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  ")
    print(abbe_number)
    
    #calling function for query function
    name_formula(abbe_sellmeier3,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)










#abbe number
def abbe_sellmeier4(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = (A0 + A1*wavelength*wavelength/(wavelength*wavelength - A2) + (A3*wavelength*wavelength/(wavelength*wavelength - A4)))**(1/2)
    return n
def sellmeier4(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = (A0 + (A1*wavelength*wavelength/((wavelength*wavelength) - A2)) + (A3*wavelength*wavelength/((wavelength*wavelength) - A4)))**(1/2)
    plot(n,wavelength,glass_name,formula_number)

    #abbe number
    #def abbe_sellmeier4(wavelength):
        #n = (A0 + A1*wavelength*wavelength/(wavelength*wavelength - A2) + (A3*wavelength*wavelength/(wavelength*wavelength - A4)))**(1/2)
        #return n
        
    abbe_number = (abbe_sellmeier4(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_sellmeier4(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_sellmeier4(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  ")
    print(abbe_number)
    
    #calling function for query function
    name_formula(abbe_sellmeier4,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)









#abbe number
def abbe_sellmeier5(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = (1.00000000 + (A0*wavelength*wavelength/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3))  + (A4*wavelength*wavelength/(wavelength*wavelength - A5)) + (A6*wavelength*wavelength/(wavelength*wavelength - A7)) + (A8*wavelength*wavelength/(wavelength*wavelength - A9)))**(1/2)
    return n
def sellmeier5(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = (1.00000000 + (A0*wavelength*wavelength/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3))  + (A4*wavelength*wavelength/(wavelength*wavelength - A5)) + (A6*wavelength*wavelength/(wavelength*wavelength - A7)) + (A8*wavelength*wavelength/(wavelength*wavelength - A9)))**(1/2)
    plot(n,wavelength,glass_name,formula_number)

    #abbe number
    #def abbe_sellmeier5(wavelength):
        #n = (1.00000000 + (A0*wavelength*wavelength/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3))  + (A4*wavelength*wavelength/(wavelength*wavelength - A5)) + (A6*wavelength*wavelength/(wavelength*wavelength - A7)) + (A8*wavelength*wavelength/(wavelength*wavelength - A9)))**(1/2)
        #return n
        
    abbe_number = (abbe_sellmeier5(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_sellmeier5(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_sellmeier5(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  ")
    print(abbe_number)

    #calling function for query function
    name_formula(abbe_sellmeier5,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)










#abbe number
def abbe_herzberger(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = ( A0 + A1*(1/((wavelength*wavelength)-0.028)) + A2*(1/((wavelength*wavelength)-0.028))*(1/((wavelength*wavelength)-0.028)) + A3*wavelength*wavelength + A4*wavelength*wavelength*wavelength*wavelength + A5*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)**(1/2)
    return n
def herzberger(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ( A0 + A1*(1/((wavelength*wavelength)-0.028)) + A2*(1/((wavelength*wavelength)-0.028))*(1/((wavelength*wavelength)-0.028)) + A3*wavelength*wavelength + A4*wavelength*wavelength*wavelength*wavelength + A5*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)**(1/2)
    plot(n,wavelength,glass_name,formula_number)

    #abbe number
    #def abbe_herzberger(wavelength):
        #n = ( A0 + A1*(1/((wavelength*wavelength)-0.028)) + A2*(1/((wavelength*wavelength)-0.028))*(1/((wavelength*wavelength)-0.028)) + A3*wavelength*wavelength + A4*wavelength*wavelength*wavelength*wavelength + A5*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)**(1/2)
        #return n
        
    abbe_number = (abbe_herzberger(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_herzberger(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_herzberger(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  ")
    print(abbe_number)
    
    #calling function for query function
    name_formula(abbe_herzberger,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)









#abbe number
def abbe_conrady(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = ( A0 + A1/(wavelength) + (A2/(wavelength)**(3.5)))
    return n
def conrady(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ( A0 + A1/(wavelength) + (A2/(wavelength)**(3.5)))
    plot(n,wavelength,glass_name,formula_number)

    #abbe number
    #def abbe_conrady(wavelength):
        #n = ( A0 + A1/(wavelength) + (A2/(wavelength)**(3.5)))
        #return n
        
    abbe_number = (abbe_conrady(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_conrady(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_conrady(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  ")
    print(abbe_number)

    #calling function for query function
    name_formula(abbe_conrady,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)










#abbe number
def abbe_handbook_optics1(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = ((A0 + A1/((wavelength*wavelength)-A2) - A3*wavelength*wavelength))**(1/2)
    return n
def handbook_optics1(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0 + A1/((wavelength*wavelength)-A2) - A3*wavelength*wavelength))**(1/2)
    plot(n,wavelength,glass_name,formula_number)

    #abbe number
    #def abbe_handbook_optics1(wavelength):
        #n = ((A0 + A1/((wavelength*wavelength)-A2) - A3*wavelength*wavelength))**(1/2)
        #return n
        
    abbe_number = (abbe_handbook_optics1(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_handbook_optics1(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_handbook_optics1(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  ")
    print(abbe_number)

    #calling function for query function
    name_formula(abbe_handbook_optics1,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)









#abbe number
def abbe_handbook_optics2(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = ((A0 + (A1*wavelength*wavelength)/((wavelength*wavelength)-A2) - A3*wavelength*wavelength))**(1/2)
    return n
def handbook_optics2(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0 + (A1*wavelength*wavelength)/((wavelength*wavelength)-A2) - A3*wavelength*wavelength))**(1/2)
    plot(n,wavelength,glass_name,formula_number)

    #abbe number
    #def abbe_handbook_optics2(wavelength):
        #n = ((A0 + (A1*wavelength*wavelength)/((wavelength*wavelength)-A2) - A3*wavelength*wavelength))**(1/2)
        #return n
        
    abbe_number = (abbe_handbook_optics2(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_handbook_optics2(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_handbook_optics2(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  ")
    print(abbe_number)

    #calling function for query function
    name_formula(abbe_handbook_optics2,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
    







#abbe number
def abbe_extended1(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A7/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    return n
def extended1(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A7/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    plot(n,wavelength,glass_name,formula_number)

    #abbe number
    #def abbe_extended1(wavelength):
        #n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A7/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
        #return n
        
    abbe_number = (abbe_extended1(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_extended1(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_extended1(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  ")
    print(abbe_number)

    #calling function for query function
    name_formula(abbe_extended1,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)









#abbe number
def abbe_extended2(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6*wavelength*wavelength*wavelength*wavelength) + (A7*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength))**(1/2)
    return n
def extended2(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6*wavelength*wavelength*wavelength*wavelength) + (A7*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength))**(1/2)
    plot(n,wavelength,glass_name,formula_number)

    #abbe number
    #def abbe_extended2(wavelength):
        #n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6*wavelength*wavelength*wavelength*wavelength) + (A7*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength))**(1/2)
        #return n
        
    abbe_number = (abbe_extended2(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_extended2(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_extended2(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  ")
    print(abbe_number)

    #calling function for query function
    name_formula(abbe_extended2,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)







#abbe number
def abbe_extended3(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2*wavelength*wavelength*wavelength*wavelength) + (A3/(wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A7/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A8/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    return n
def extended3(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2*wavelength*wavelength*wavelength*wavelength) + (A3/(wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A7/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A8/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    plot(n,wavelength,glass_name,formula_number)
    
    #abbe number
    #def abbe_extended3(wavelength):
        #n = ((A0) + (A1*(wavelength*wavelength)) + (A2*wavelength*wavelength*wavelength*wavelength) + (A3/(wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A7/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A8/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
        #return n
        
    abbe_number = (abbe_extended3(0.5892,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-1)/(abbe_extended3(0.4861,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)-abbe_extended3(0.6563,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
    print("Abbe number of this glass type is  ")
    print(abbe_number)

    #calling function for query function
    name_formula(abbe_extended3,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        
        
    
    



#to check formula number and name         
def formula_name(formula_name1,glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
        if formula_name1 == 'schott':
            schott(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        if formula_name1 == 'sellmeier1':
            sellmeier1(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        if formula_name1 == 'sellmeier2':
            sellmeier2(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)    
        if formula_name1 == 'sellmeier3':
            sellmeier3(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        if formula_name1 == 'sellmeier4':
            sellmeier4(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        if formula_name1 == 'sellmeier5':
            sellmeier5(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        if formula_name1 == 'herzberger':
            herzberger(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        if formula_name1 == 'condrady':
            conrady(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        if formula_name1 == 'handbook_optics1':
            handbook_optics1(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        if formula_name1 == 'handbook_optics2':
            handbook_optics2(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        if formula_name1 == 'extended1':
            extended1(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        if formula_name1 == 'extended2':
            extended2(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        if formula_name1 == 'extended3':
            extended3(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            







#purpose of this function to find RI for thermal analysis          
def formula_thermal_name(formula_name1,wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
        if formula_name1 == 'schott':   
            n0 = abbe_schott(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
        if formula_name1 == 'sellmeier1':   
            n0 = abbe_sellmeier1(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
        if formula_name1 == 'sellmeier2'  :
            n0 = abbe_sellmeier2(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
        if formula_name1 == 'sellmeier3':   
            n0 = abbe_sellmeier3(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
        if formula_name1 == 'sellmeier4':  
            n0 = abbe_sellmeier4(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
        if formula_name1 == 'sellmeier5':  
            n0 = abbe_sellmeier5(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
        if formula_name1 == 'herzberger':  
            n0 = abbe_herzberger(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
        if formula_name1 == 'condrady':    
            n0  = abbe_conrady(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
        if formula_name1 == 'handbook_optics1':
            n0 = abbe_handbook_optics1(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
        if formula_name1 == 'handbook_optics2':
            n0 = abbe_handbook_optics2(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
        if formula_name1 == 'extended1':     
            n0 = abbe_extended1(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
        if formula_name1 == 'extended2':
            n0 = abbe_extended2(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
        if formula_name1 == 'extended3':
            n0 = abbe_extended3(wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            return n0
