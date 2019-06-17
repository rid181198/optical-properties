# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:27:35 2019

@author: crystal
"""
import os
import numpy as np
import Formulas as formula_file
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from itertools import cycle
import csv
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
            plt.ylabel('Derivative of n_abs(10^-6)' , fontsize = 14)
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
            plt.ylabel('Derivative of n_rel(10^-6)' , fontsize = 14)
            plt.legend()
            plt.savefig(os.path.abspath('Plots\\'+'n_rel_derivative_vs_temperature'+plot_name3+'.png'))
        
        else:
            break
    plt.show()    


def verification_thermal(glass_name,temperature_list,formula_number,formula_name1,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9):
    
    if glass_name == 'N-BK7' or glass_name == 'F2' or glass_name == 'N-PK51' or glass_name == 'SF57' or glass_name == 'N-LAF2':
    
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
                
        
        #verification for n_abs_derivative
        while True:
            response = input("Do you want to verification of the derivative of absolute change in refractive index only for N-BK7,F2,N-LAF2,N-PK51,SF57  at 1060 nm wavelength (y/n) :  ")
            if response == 'y':
                
                #give the value of wavelength
                wavelength = float(1060)
                wavelength=wavelength/1000
                
                #open the file
                with open(os.path.abspath('Data\\Verification_of_temperature_effect\\Temp_data\\'+glass_name+'\\'+glass_name+'.txt'))  as file:
                    
                    #make the list of data
                    file_content = file.read()
                    file_content_list = file_content.split()
                    index = file_content_list.index('#1')
                    #given data
                    data_list = file_content_list[(index+1) : ]
                    #print(data_list)
                    
                    #calculated data list
                    data_cal_n_list =[]
                    temp_list=[]
                    for i in range(0,len(data_list),2):
                        #temperature
                        T=float(data_list[i])
                        temp_list.append(data_list[i])
                        
                        #refractive index at reference temperature
                        n0 = formula_file.formula_thermal_name(formula_name1,wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
                
                        #putting in formulas
                        n_abs_derivative = ((((n0*n0)-1.00)/(2.00*n0))*(D0 + (2.00*D1*(T-T0)) + (3.00*D2*(T-T0)*(T-T0)) + ((E0 + (2.00*E1*(T-T0)))/((wavelength*wavelength)-(Ltk*Ltk))) ))
                        n_abs_dcon_cal = (n_abs_derivative)*1000000
                        data_cal_n_list.append(n_abs_dcon_cal)
                    
                    #make the list for given data
                    data_giv_n_list=[]
                    for i in range(1,len(data_list),2):
                        data_giv_n_list.append(data_list[i])
                    
                    #print the table for verification
                    print("Table is for glass type " + glass_name)
                    print("wavelength is ",end=' ')
                    print(wavelength*1000)
                    
                    with open(os.path.abspath("Plots\\Verification\\" + 'derivative_n_abs_change_verify.csv'),mode = 'w') as data:
                        file = csv.writer(data)
                        file.writerow(["Given change in reference","Calculated by formula","Difference(10^-6)"])
                        #make the diff list    
                        diff_list=[]
                        for i in range(0,len(data_giv_n_list),1):
                            diff = float(data_giv_n_list[i]) - float(data_cal_n_list[i])
                            diff_list.append(diff)
                            table = PrettyTable()
                            table.field_names = ["Given change in reference","Calculated by formula", "Difference(10^-6)"]
                            table.add_row([data_giv_n_list[i],data_cal_n_list[i],diff])
                            print(table)
                            
                            #save the file
                            file.writerow([data_giv_n_list[i],data_cal_n_list[i],diff_list[i]])
                    
                    #plot the difference
                    plt.figure(figsize=(15,10))
                    for i in range(0,len(data_giv_n_list),1):
    
                        plt.scatter((float(temp_list[i])),(float(diff_list[i])),s=60)
                        plt.title(glass_name)
                        plt.xlabel("Temperature (C)",fontsize = 14)
                        plt.xticks(rotation = 90)
                        plt.ylabel('Difference of derivative of absolute refractive index(10^-6)' , fontsize = 12)
                        
                        plt.savefig(os.path.abspath('Plots\\Verification\\'+'derivative_n_abs_change_plot.png'))
                    plt.show()
              
            else:
                break
        
        #verification for n_rel_derivative
        while True:
            response = input("Do you want to verification of the derivative of relative change in refractive index only for N-BK7,F2,N-LAF2,N-PK51,SF57  at 1060 nm wavelength (y/n) :  ")
            if response == 'y':
                
                #give the value of wavelength
                wavelength = float(1060)
                wavelength=wavelength/1000
                P=float(101330)
                
                #open the file
                with open(os.path.abspath('Data\\Verification_of_temperature_effect\\Temp_data\\'+glass_name+'\\'+glass_name+'_2.txt'))  as file:
                    
                    #make the list of data
                    file_content = file.read()
                    file_content_list = file_content.split()
                    index = file_content_list.index('#1')
                    #given data
                    data_list = file_content_list[(index+1) : ]
                    #print(data_list)
                    
                    #calculated data list
                    data_cal_n_list =[]
                    temp_list=[]
                    for i in range(0,len(data_list),2):
                        #temperature
                        T=float(data_list[i])
                        temp_list.append(data_list[i])
                        
                        #refractive index at reference temperature
                        n0 = formula_file.formula_thermal_name(formula_name1,wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
                
                        #putting in formulas
                        n_rel_derivative = ((((((((n0*n0)-1.00)/(2.00*n0))*(D0 + (2.00*D1*(T-T0)) + (3.00*D2*(T-T0)*(T-T0)) + ((E0 + (2.00*E1*(T-T0)))/((wavelength*wavelength)-(Ltk*Ltk))) ))) - ((((n0  +  ((((((n0*n0)-1.00)/(2.00*n0))*((D0*(T-T0)) + (D1*(T-T0)*(T-T0)) + (D2*(T-T0)*(T-T0)*(T-T0)) + (((E0*(T-T0)) + (E1*(T-T0)*(T-T0)))/((wavelength*wavelength)-(Ltk*Ltk))) )))/((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T0 - 15))*101325) )))))*(((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T0 - 15))*101325) )))/((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T - 15))*101325) ) )))))*(((-0.00367)*((((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T - 15))*101325) ) ))-1)/(1+0.00367*T))))))/((1.0000  +  (((((1.0000 + ((0.00000001)*(6432.8 + ((2949810*wavelength*wavelength)/((146*wavelength*wavelength)-1.0000)) +  ((25540*wavelength*wavelength)/((41*wavelength*wavelength)-1)) )))) - 1)*P)/((1.0000 + 0.0034785*(T - 15))*101325) ) ))))
                        n_rel_dcon_cal = (n_rel_derivative)*1000000
                        data_cal_n_list.append(n_rel_dcon_cal)
                    
                    #make the list for given data
                    data_giv_n_list=[]
                    for i in range(1,len(data_list),2):
                        data_giv_n_list.append(data_list[i])
                    
                    #print the table for verification
                    print("Table is for glass type " + glass_name)
                    print("wavelength is ",end=' ')
                    print(wavelength*1000)
                    
                    with open(os.path.abspath("Plots\\Verification\\" + 'derivative_n_rel_change_verify.csv'),mode = 'w') as data:
                        file = csv.writer(data)
                        file.writerow(["Given change in reference","Calculated by formula","Difference(10^-6)"])
                        #make the diff list    
                        diff_list=[]
                        for i in range(0,len(data_giv_n_list),1):
                            diff = float(data_giv_n_list[i]) - float(data_cal_n_list[i])
                            diff_list.append(diff)
                            table = PrettyTable()
                            table.field_names = ["Given change in reference","Calculated by formula", "Difference(10^-6)"]
                            table.add_row([data_giv_n_list[i],data_cal_n_list[i],diff])
                            print(table)
                            
                            #save the file
                            file.writerow([data_giv_n_list[i],data_cal_n_list[i],diff_list[i]])
                    
                    #plot the difference
                    plt.figure(figsize=(15,10))
                    for i in range(0,len(data_giv_n_list),1):
    
                        plt.scatter(float(temp_list[i]),(float(diff_list[i])),s=60)
                        plt.title(glass_name)
                        plt.xlabel("Temperature (C)",fontsize = 14)
                        plt.xticks(rotation = 90)
                        plt.ylabel('Difference of derivative of relative refractive index (10^-6)' , fontsize = 12)
                    
                        plt.savefig(os.path.abspath('Plots\\Verification\\'+'derivative_n_rel_change_plot.png'))
                    plt.show()
              
            else:
                break
    
    
    
    
