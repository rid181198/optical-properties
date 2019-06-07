# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:27:35 2019

@author: crystal
"""
import os
import numpy as np
import Formulas as formula_file
import matplotlib.pyplot as plt
from itertools import cycle
color_cycle = cycle('bgrcmk')


def thermal_describtion_glass(glass_name,temperature_list,formula_number,formula_name1,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
   
    #display all thermal coefficients
    print("\nThermal coefficients are  ,")
    print("\nD0 :  " + temperature_list[1])
    print("\nD1 :  " + temperature_list[2])
    print("\nD2 :  " + temperature_list[3])
    print("\nE0 :  " + temperature_list[4])
    print("\nE1 :  " + temperature_list[5])
    print("\n\u03BB(Tk)  :  " + temperature_list[6])
    print("\nReference temperature T0 :  " + temperature_list[7])
    
    #assigning values 
    D0 = float(temperature_list[1])
    D1 = float(temperature_list[2])
    D2 = float(temperature_list[3])
    E0 = float(temperature_list[4])
    E1 = float(temperature_list[5])
    Ltk = float(temperature_list[6])
    #reference temperature in celcius
    T0 = float(temperature_list[7])
    
    
    
    while True:
        response = input("Do you want to comparision with different wavelengths of same glass type for DERIVATIVE OF ABSOLUTE REFRACTIVE INDEX WITH TEMPERATURE(y/n)  :  ")
        if response == 'y':
          
            #get input of wavelength in nanometer and temperature in celcius
            #T = temperature = float(input("\nPlease enter the temperature in celcius for thermal analysis  :   "))
            wavelength = float(input("\nPlease enter the wavelength in (nm) for thermal analysis  :  "))
            wavelength = wavelength/1000
    
            #print the refractive index of particular wavelength at reference temperature
            n0 = formula_file.formula_thermal_name(formula_name1,wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            print("\nRefractive index at reference temperature is n0 :  ",end= ' ')
            print(float(n0))
    
            #plot of derivative of absolute refractive index with temperature
            plot_name = str(glass_name+ '_'+formula_number)
            T = np.arange(-100.00,140.00,0.01)
            n_abs_derivative = ((((n0*n0)-1.00)/(2.00*n0))*(D0 + (2.00*D1*(T-T0)) + (3.00*D2*(T-T0)*(T-T0)) + ((E0 + (2.00*E1*(T-T0)))/((wavelength*wavelength)-(Ltk*Ltk))) ))
            n_abs_dcon = (n_abs_derivative)*1000000
            plt.plot(T,n_abs_dcon,'r-',label = float(wavelength)*1000,c=next(color_cycle))
            plt.xlabel('Surface Temperature',fontsize = 14)
            plt.ylabel('Derivative of n_abs' , fontsize = 14)
            plt.legend()
            plt.savefig(os.path.abspath('Plots\\'+'n_abs_derivative_vs_temperature'+plot_name+'.png'))
            
        else :
            break
   
    plt.show()  
    
    while True:
        response = input("Do you want to get refractive index at specific temperature (y/n) : ")
        if response == 'y' :
            
            #Find the refractive index at any temperature
            wavelength = float(input("Please enter the wavelength in nm  :  "))
            wavelength = wavelength/1000
            P = float(input("\nEnter the pressure (Pa) to find refractive index :  "))
            T= float(input("\nEnter the temperature to find refractive index : "))
    
            #print the refractive index of particular wavelength at reference temperature
            n0 = formula_file.formula_thermal_name(formula_name1,wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            print("\nRefractive index at reference temperature is n0 :  ",end= '')
            print(float(n0))
            print("Temperature is :  ",end= ' ' )
            print(T0)
            
            #required equations
            #change of absolute refractive index with temperature
            n_abs_change = ((((n0*n0)-1.00)/(2.00*n0))*((D0*(T-T0)) + (D1*(T-T0)*(T-T0)) + (D2*(T-T0)*(T-T0)*(T-T0)) + (((E0*(T-T0)) + (E1*(T-T0)*(T-T0)))/((wavelength*wavelength)-(Ltk*Ltk))) ))
            
            #refractive index(air) at temperature 15 and pressure 101330 Pa
            n_air_15 = (1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))
            
            #refractive index(air) at temperature T0 and pressure 101330 Pa
            n_air_catT0 = (1.0000  +  (((n_air_15 - 1)*P)/((1.0000 + 0.0034785*(T0 - 15))*101325) ))
            
            #refractive index(air) at temperature T and Pressure P Pa
            n_air_catT = (1.0000  +  (((n_air_15 - 1)*P)/((1.0000 + 0.0034785*(T - 15))*101325) ) )
            
            n_rel_givenT = (n0  +  (n_abs_change/n_air_catT0))*(n_air_catT0/n_air_catT)
            
            print("\nRefractive index at given temperature is : ",end = ' ' )
            print(n_rel_givenT)
            print("Temperature is :  ",end =' ')
            print(T)
        else :
            break
    
    while True:
        response = input("Do you want to get plot between refractive index and temperature (y/n) :  ")
        if response == 'y':
            
             
            wavelength = float(input("Please enter the wavelength in nm  :  "))
            wavelength = wavelength/1000
            P = float(input("\nEnter the pressure (Pa) to find refractive index :  "))
            #print the refractive index of particular wavelength at reference temperature
            n0 = formula_file.formula_thermal_name(formula_name1,wavelength,\
                                                   A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            
            plot_name2 = str(glass_name+ '_'+formula_number)
            T = np.arange(-100,140,0.01)
            n_rel_givenT = ((n0  +  ((((((n0*n0)-1.00)/(2.00*n0))*((D0*(T-T0)) + (D1*(T-T0)*(T-T0)) + (D2*(T-T0)*(T-T0)*(T-T0)) + (((E0*(T-T0)) + (E1*(T-T0)*(T-T0)))/((wavelength*wavelength)-(Ltk*Ltk))) )))/((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T0 - 15))*101325) )))))*(((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T0 - 15))*101325) )))/((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T - 15))*101325) ) ))))
            plt.plot(T,n_rel_givenT,'r-',label = float(wavelength)*1000,c=next(color_cycle))
            plt.xlabel("Temperature")
            plt.ylabel("Refractive index")
            plt.legend()
            plt.savefig(os.path.abspath('Plots\\'+'n_vs_temperature'+plot_name2+'.png'))
        else :
            break
    plt.show()
    
    #plot for relative change
    while True:
        response = input("Do you want to get comaparison between different wavelengths of same glass type for DERIVATIVE OF RELATIVE REFRACTIVE INDEX CHANGE WITH TEMPERATURE (y/n) :  ")
        if response == 'y':
            
            #get input of wavelength in nanometer
            wavelength = float(input("\nPlease enter the wavelength in (nm) for thermal analysis  :  "))
            wavelength = wavelength/1000
            #pressure
            P = float(input("\nEnter the pressure (Pa) to find refractive index :  "))
            
            #print the refractive index of particular wavelength at reference temperature
            n0 = formula_file.formula_thermal_name(formula_name1,wavelength,\
                                                   A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            print("\nRefractive index at reference temperature is n0 :  ",end= '')
            print(float(n0))
            
            #derivative of refractive index of air 
            #n_air_derivative = ((-0.00367)*((n_air_catT-1)/(1+0.00367*T)))
            
            #plot of derivative of absolute refractive index with temperature
            plot_name3 = str(glass_name+ '_'+formula_number)
            T = np.arange(-100.00,140.00,0.01)
          
            n_rel_derivative = ((((((((n0*n0)-1.00)/(2.00*n0))*(D0 + (2.00*D1*(T-T0)) + (3.00*D2*(T-T0)*(T-T0)) + ((E0 + (2.00*E1*(T-T0)))/((wavelength*wavelength)-(Ltk*Ltk))) ))) - ((((n0  +  ((((((n0*n0)-1.00)/(2.00*n0))*((D0*(T-T0)) + (D1*(T-T0)*(T-T0)) + (D2*(T-T0)*(T-T0)*(T-T0)) + (((E0*(T-T0)) + (E1*(T-T0)*(T-T0)))/((wavelength*wavelength)-(Ltk*Ltk))) )))/((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T0 - 15))*101325) )))))*(((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T0 - 15))*101325) )))/((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T - 15))*101325) ) )))))*(((-0.00367)*((((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T - 15))*101325) ) ))-1)/(1+0.00367*T))))))/((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T - 15))*101325) ) ))))*1000000  
            plt.plot(T,n_rel_derivative,'r-',label = (float(wavelength)*1000),c=next(color_cycle))
            plt.xlabel('Surface Temperature',fontsize = 14)
            plt.ylabel('Derivative of n_rel' , fontsize = 14)
            plt.legend()
            plt.savefig(os.path.abspath('Plots\\'+'n_rel_derivative_vs_temperature'+plot_name3+'.png'))
        
        else:
            break
    plt.show()          
            
            
            
    
    
    
    
    
    
    
