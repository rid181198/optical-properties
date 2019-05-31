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
     print('\nGlass dispersion formula number is ' + formula_number + ' and dispersion formula is ' + glass_name)
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
         





def sellmeier1(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = np.sqrt(1.0000000000 + (A0*(wavelength*wavelength)/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3)) + (A4*wavelength*wavelength/(wavelength*wavelength - A5)))  
    plot(n,wavelength)
    
    
def sellmeier2(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = (1.0000000 + A0 + A1*(wavelength*wavelength)/((wavelength*wavelength)-(A2*A2)) + A3/((wavelength*wavelength)-(A4*A4)))**(1/2)
    plot(n,wavelength)




def sellmeier3(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = (1.0000000000 + (A0*(wavelength*wavelength)/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3)) + (A4*wavelength*wavelength/(wavelength*wavelength - A5)) + (A6*wavelength*wavelength/(wavelength*wavelength - A7)))**(1/2)  
    plot(n,wavelength)
    plot(n,wavelength)




def sellmeier4(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = (A0 + A1*wavelength*wavelength/(wavelength*wavelength - A2) + (A3*wavelength*wavelength/(wavelength*wavelength - A4)))**(1/2)
    plot(n,wavelength)




def sellmeier5(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = (1.00000000 + (A0*wavelength*wavelength/(wavelength*wavelength - A1)) + (A2*wavelength*wavelength/(wavelength*wavelength - A3))  + (A4*wavelength*wavelength/(wavelength*wavelength - A5)) + (A6*wavelength*wavelength/(wavelength*wavelength - A7)) + (A8*wavelength*wavelength/(wavelength*wavelength - A9)))**(1/2)
    plot(n,wavelength)





def herzberger(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ( A0 + A1*(1/((wavelength*wavelength)-0.028)) + A2*(1/((wavelength*wavelength)-0.028))*(1/((wavelength*wavelength)-0.028)) + A3*wavelength*wavelength + A4*wavelength*wavelength*wavelength*wavelength + A5*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)**(1/2)
    plot(n,wavelength)




def condrady(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ( A0 + A1/(wavelength) + (A2/(wavelength)**(3.5)))
    plot(n,wavelength)




def schott(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    plot(n,wavelength)




def schott(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    plot(n,wavelength)




def schott(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    plot(n,wavelength)




def schott(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    plot(n,wavelength)



def schott(glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    describtion_glass(glass_name,formula_number,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
 
    #plot
    wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
    n = ((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
    plot(n,wavelength)
    
 

     
                                                            