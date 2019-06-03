# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:00:25 2019

@author: crystal
"""

import numpy as np
import matplotlib.pyplot as plt
#def main_func():
  #  print('Hello World')
    
    
#if __name__=="__main__":
 #   main_func()
 
 
#defining function or data set for each formula
def describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
     #details of glass    
     print('\nGlass dispersion formula number is ' + formula_number)
     print("\nConstants values for  are, \n\nA0 : ")
     print(A0)
     print('\nA1 : ' )
     print(A1)
     print('\nA2 : ' )
     print(A2)
     print('\nA3 : ' )
     print(A3)
     print('\nA4 : ' )
     print(A4)
     print('\nA5 : ' )
     print(A5)
     print('\nA6 : ' )
     print(A6)
     print('\nA7 : ' )
     print(A7)
     print('\nA8 : ' )
     print(A8)
     print('\nA9 : ' )
     print(A9)
    


def plot(n,wavelength):
     wavelength_nanometer=wavelength*1000
     plt.plot(wavelength_nanometer,n,'r-')
     plt.xlabel('Wavelength \u03BB (nm) ' , fontsize= 14)
     plt.ylabel('Refractive Index n ' , fontsize = 14 )
     
     
     

#formulas for all dispersion 
def schott(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    plot(n,wavelength)
    
    #abbe number
    def abbe_schott(wavelength):
        n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
        return n
        
    abbe_number = (abbe_schott(0.5892)-1)/(abbe_schott(0.4861)-abbe_schott(0.6563))
    print("Abbe number of this glass type is  " )
    print(abbe_number) 
    
    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000
            print("\nwavelength is  ")
            print(abbe_schott(wavelength))
        else:
            break 
    

    



def sellmeier1(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = np.sqrt(1.0000000000 + (A0*(wavelength*wavelength)/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3)) + (A4*wavelength*wavelength/(wavelength*wavelength - A5)))  
    plot(n,wavelength)
    
    #abbe number
    def abbe_sellmeier1(wavelength):
        n = np.sqrt(1.0000000000 + (A0*(wavelength*wavelength)/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3)) + (A4*wavelength*wavelength/(wavelength*wavelength - A5)))
        return n
        
    abbe_number = (abbe_sellmeier1(0.5892)-1)/(abbe_sellmeier1(0.4861)-abbe_sellmeier1(0.6563))
    print("Abbe number of this glass type is  ")
    print(abbe_number)
    
    
    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000
            print("\nwavelength is  ")
            print(abbe_sellmeier1(wavelength)) 
        else:
            break 

    
    




def sellmeier2(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = (1.0000000 + A0 + A1*(wavelength*wavelength)/((wavelength*wavelength)-(A2*A2)) + A3/((wavelength*wavelength)-(A4*A4)))**(1/2)
    plot(n,wavelength)

    #abbe number
    def abbe_sellmeier2(wavelength):
        n = (1.0000000 + A0 + A1*(wavelength*wavelength)/((wavelength*wavelength)-(A2*A2)) + A3/((wavelength*wavelength)-(A4*A4)))**(1/2)
        return n
        
    abbe_number = (abbe_sellmeier2(0.5892)-1)/(abbe_sellmeier2(0.4861)-abbe_sellmeier2(0.6563))
    print("Abbe number of this glass type is  ")
    print(abbe_number)
    
    
    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000
            print("\nwavelength is  ")
            print(abbe_sellmeier2(wavelength)) 
        else:
            break 
    




def sellmeier3(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = (1.0000000000 + (A0*(wavelength*wavelength)/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3)) + (A4*wavelength*wavelength/(wavelength*wavelength - A5)) + (A6*wavelength*wavelength/(wavelength*wavelength - A7)))**(1/2)  
    plot(n,wavelength)
    plot(n,wavelength)

    #abbe number
    def abbe_sellmeier3(wavelength):
        n = (1.0000000000 + (A0*(wavelength*wavelength)/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3)) + (A4*wavelength*wavelength/(wavelength*wavelength - A5)) + (A6*wavelength*wavelength/(wavelength*wavelength - A7)))**(1/2)
        return n
        
    abbe_number = (abbe_sellmeier3(0.5892)-1)/(abbe_sellmeier3(0.4861)-abbe_sellmeier3(0.6563))
    print("Abbe number of this glass type is  ")
    print(abbe_number)
    
    
    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000

            print("\nwavelength is  ")
            print(abbe_sellmeier3(wavelength)) 
        else:
            break 






def sellmeier4(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = (A0 + A1*wavelength*wavelength/(wavelength*wavelength - A2) + (A3*wavelength*wavelength/(wavelength*wavelength - A4)))**(1/2)
    plot(n,wavelength)

    #abbe number
    def abbe_sellmeier4(wavelength):
        n = (A0 + A1*wavelength*wavelength/(wavelength*wavelength - A2) + (A3*wavelength*wavelength/(wavelength*wavelength - A4)))**(1/2)
        return n
        
    abbe_number = (abbe_sellmeier4(0.5892)-1)/(abbe_sellmeier4(0.4861)-abbe_sellmeier4(0.6563))
    print("Abbe number of this glass type is  ")
    print(abbe_number)


    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000
         
            print("\nwavelength is  ")
            print(abbe_sellmeier4(wavelength)) 
        else:
            break 



def sellmeier5(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = (1.00000000 + (A0*wavelength*wavelength/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3))  + (A4*wavelength*wavelength/(wavelength*wavelength - A5)) + (A6*wavelength*wavelength/(wavelength*wavelength - A7)) + (A8*wavelength*wavelength/(wavelength*wavelength - A9)))**(1/2)
    plot(n,wavelength)

    #abbe number
    def abbe_sellmeier5(wavelength):
        n = (1.00000000 + (A0*wavelength*wavelength/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3))  + (A4*wavelength*wavelength/(wavelength*wavelength - A5)) + (A6*wavelength*wavelength/(wavelength*wavelength - A7)) + (A8*wavelength*wavelength/(wavelength*wavelength - A9)))**(1/2)
        return n
        
    abbe_number = (abbe_sellmeier5(0.5892)-1)/(abbe_sellmeier5(0.4861)-abbe_sellmeier5(0.6563))
    print("Abbe number of this glass type is  ")
    print(abbe_number)

    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000
           
            print("\nwavelength is  ")
            print(abbe_sellmeier5(wavelength)) 
        else:
            break 




def herzberger(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ( A0 + A1*(1/((wavelength*wavelength)-0.028)) + A2*(1/((wavelength*wavelength)-0.028))*(1/((wavelength*wavelength)-0.028)) + A3*wavelength*wavelength + A4*wavelength*wavelength*wavelength*wavelength + A5*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)**(1/2)
    plot(n,wavelength)

    #abbe number
    def abbe_herzberger(wavelength):
        n = ( A0 + A1*(1/((wavelength*wavelength)-0.028)) + A2*(1/((wavelength*wavelength)-0.028))*(1/((wavelength*wavelength)-0.028)) + A3*wavelength*wavelength + A4*wavelength*wavelength*wavelength*wavelength + A5*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)**(1/2)
        return n
        
    abbe_number = (abbe_herzberger(0.5892)-1)/(abbe_herzberger(0.4861)-abbe_herzberger(0.6563))
    print("Abbe number of this glass type is  ")
    print(abbe_number)
    
    
    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000
         
            print("\nwavelength is  ")
            print(abbe_herzberger(wavelength)) 
        else:
            break 




def condrady(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ( A0 + A1/(wavelength) + (A2/(wavelength)**(3.5)))
    plot(n,wavelength)

    #abbe number
    def abbe_condrady(wavelength):
        n = ( A0 + A1/(wavelength) + (A2/(wavelength)**(3.5)))
        return n
        
    abbe_number = (abbe_condrady(0.5892)-1)/(abbe_condrady(0.4861)-abbe_condrady(0.6563))
    print("Abbe number of this glass type is  ")
    print(abbe_number)


    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000
           
            print("\nwavelength is  ")
            print(abbe_condrady(wavelength)) 
        else:
            break 



def handbook_optics1(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0 + A1/((wavelength*wavelength)-A2) - A3*wavelength*wavelength))**(1/2)
    plot(n,wavelength)

    #abbe number
    def abbe_handbook_optics1(wavelength):
        n = ((A0 + A1/((wavelength*wavelength)-A2) - A3*wavelength*wavelength))**(1/2)
        return n
        
    abbe_number = (abbe_handbook_optics1(0.5892)-1)/(abbe_handbook_optics1(0.4861)-abbe_handbook_optics1(0.6563))
    print("Abbe number of this glass type is  ")
    print(abbe_number)


    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000
           
            print("\nwavelength is  ")
            print(abbe_handbook_optics1(wavelength)) 
        else:
            break 


def handbook_optics2(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0 + (A1*wavelength*wavelength)/((wavelength*wavelength)-A2) - A3*wavelength*wavelength))**(1/2)
    plot(n,wavelength)

    #abbe number
    def abbe_handbook_optics2(wavelength):
        n = ((A0 + (A1*wavelength*wavelength)/((wavelength*wavelength)-A2) - A3*wavelength*wavelength))**(1/2)
        return n
        
    abbe_number = (abbe_handbook_optics2(0.5892)-1)/(abbe_handbook_optics2(0.4861)-abbe_handbook_optics2(0.6563))
    print("Abbe number of this glass type is  ")
    print(abbe_number)


    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000
            
            print("\nwavelength is  ")
            print(abbe_handbook_optics2(wavelength)) 
        else:
            break 


def extended1(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A7/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    plot(n,wavelength)

    #abbe number
    def abbe_extended1(wavelength):
        n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A7/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
        return n
        
    abbe_number = (abbe_extended1(0.5892)-1)/(abbe_extended1(0.4861)-abbe_extended1(0.6563))
    print("Abbe number of this glass type is  ")
    print(abbe_number)


    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
  
            print("\nwavelength is  ")
            print(abbe_extended1(wavelength)) 
        else:
            break 



def extended2(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6*wavelength*wavelength*wavelength*wavelength) + (A7*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength))**(1/2)
    plot(n,wavelength)

    #abbe number
    def abbe_extended2(wavelength):
        n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6*wavelength*wavelength*wavelength*wavelength) + (A7*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength))**(1/2)
        return n
        
    abbe_number = (abbe_extended2(0.5892)-1)/(abbe_extended2(0.4861)-abbe_extended2(0.6563))
    print("Abbe number of this glass type is  ")
    print(abbe_number)


    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000
           
            print("\nwavelength is  ")
            print(abbe_extended2(wavelength)) 
        else:
            break 



def extended3(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2*wavelength*wavelength*wavelength*wavelength) + (A3/(wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A7/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A8/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    plot(n,wavelength)
    
    #abbe number
    def abbe_extended3(wavelength):
        n = ((A0) + (A1*(wavelength*wavelength)) + (A2*wavelength*wavelength*wavelength*wavelength) + (A3/(wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A6/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A7/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A8/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
        return n
        
    abbe_number = (abbe_extended3(0.5892)-1)/(abbe_extended3(0.4861)-abbe_extended3(0.6563))
    print("Abbe number of this glass type is  ")
    print(abbe_number)

    
    #query
    while True:
        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
        if get_refractive_index == 'y':
            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
            wavelength = float(wavelength)/1000
       
            print("\nwavelength is  ")
            print(abbe_extended3(wavelength)) 
        else:
            break 
        
        
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
            condrady(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
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
            
        else :
            print("There is no dispersion formula for this glass type")