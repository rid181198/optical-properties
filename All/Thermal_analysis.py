# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:27:35 2019

@author: crystal
"""
import numpy as np
import Formulas as formula_file
import matplotlib.pyplot as plt
def thermal_describtion_glass(temperature_list,formula_number,formula_name1,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    #get input of wavelength in nanometer and temperature in celcius
    #T = temperature = float(input("\nPlease enter the temperature in celcius for thermal analysis  :   "))
    wavelength = float(input("\nPlease enter the wavelength in (nm) for thermal analysis  :  "))
    wavelength = wavelength/1000
    
    #display all thermal coefficients
    print("\nThermal coefficients are  ,")
    print("\nD0 :  " + temperature_list[1])
    print("\nD1 :  " + temperature_list[2])
    print("\nD2 :  " + temperature_list[3])
    print("\nE0 :  " + temperature_list[4])
    print("\nE1 :  " + temperature_list[5])
    print("\n\u03BB(Tk)  :  " + temperature_list[6])
    print("\nReference temperature T0 :  " + temperature_list[7])
    
    #print the refractive index of particular wavelength at reference temperature
    n0 = formula_file.formula_thermal_name(formula_name1,wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
    print("\nRefractive index at reference temperature is n0 :  ",end= '')
    print(float(n0))
    
    #assigning values 
    D0 = float(temperature_list[1])
    D1 = float(temperature_list[2])
    D2 = float(temperature_list[3])
    E0 = float(temperature_list[4])
    E1 = float(temperature_list[5])
    Ltk = float(temperature_list[6])
    #reference temperature in celcius
    T0 = float(temperature_list[7])
    #delT = T - T0
    
    
    T = np.arange(-100.00,140.00,0.01)
    n_abs_derivative = ((((n0*n0)-1.00)/(2.00*n0))*(D0 + (2.00*D1*(T-T0)) + (3.00*D2*(T-T0)*(T-T0)) + ((E0 + (2.00*E1*(T-T0)))/((wavelength*wavelength)-(Ltk*Ltk))) ))
    n_abs_dcon = (n_abs_derivative)*1000000
    plt.plot(T,n_abs_dcon,'r-')
    plt.xlabel('Surface Temperature',fontsize = 14)
    plt.ylabel('Derivative of n_abs' , fontsize = 14)
    plt.show()
    
    
    
    
    
    
