# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:22:56 2019

@author: crystal
"""
import os
import Formulas as formula_file

#T = temperature of surrounding
#P = Pressure of surrounding
#please enter the wavelength in nm, temperature in celcius and pressure in Pa
def thermal_describtion_glass(glass_name,wavelength,P,T):
    
    wavelength=wavelength/1000
    #open the directory and files
    for filename in os.listdir(os.path.abspath('AGF\\')):
        file_name_string=str(filename)
    
        #open each of the file here file_string is name of the each file
        with open(os.path.abspath('AGF\\'+file_name_string)) as file:
        
            #file_contents_list is list of contents of files
            contents=file.read()
            file_contents_list = contents.split()
        
        #check the condition for name in that list
        if glass_name in file_contents_list :    
            #print the glass name
            print('\nGlass name is in the '+ file_name_string + ' catalog')
            print('\nGlass name is ' + glass_name)
         
            #find the index of the glass name
            glass_name_index=int(file_contents_list.index(glass_name))
                             
            #find the index of formula number
            formula_number=file_contents_list[glass_name_index+1]
        
            j=0    
            with open(os.path.abspath('AGF\\'+file_name_string)) as file:
                 file_lines_list = file.readlines()
        
            for file_lines in file_lines_list:
                #find the details of the glass
                file_lines_wordlist = file_lines.split()
                if glass_name in file_lines_wordlist :
                 
                    for file_lines in file_lines_list[j:j+20]: 
                 
                        #display constants for formula
                        if 'CD' in file_lines:
                            constants_list = file_lines.split()
                            length_constants = len(constants_list)
            
                        #temperature list     
                        if 'TD' in file_lines:
                            temperature_list = file_lines.split()
                            
                j=j+1
                      
           
            #define the constants as per length of line in the file
            if length_constants == 11:
                 A0 = float(constants_list[1])
                 A1 = float(constants_list[2])
                 A2 = float(constants_list[3])
                 A3 = float(constants_list[4])
                 A4 = float(constants_list[5])
                 A5 = float(constants_list[6])
                 A6 = float(constants_list[7])
                 A7 = float(constants_list[8])
                 A8 = float(constants_list[9])
                 A9 = float(constants_list[10])
            if length_constants == 10:
            
                 A0 = float(constants_list[1])
                 A1 = float(constants_list[2])
                 A2 = float(constants_list[3])
                 A3 = float(constants_list[4])
                 A4 = float(constants_list[5])
                 A5 = float(constants_list[6])
                 A6 = float(constants_list[7])
                 A7 = float(constants_list[8])
                 A8 = float(constants_list[9])
                 A9=0

            if length_constants == 9:
    
                 A0 = float(constants_list[1])
                 A1 = float(constants_list[2])
                 A2 = float(constants_list[3])
                 A3 = float(constants_list[4])
                 A4 = float(constants_list[5])
                 A5 = float(constants_list[6])
                 A6 = float(constants_list[7])
                 A7 = float(constants_list[8])
                 A8=A9=0
             
            if length_constants == 8 :
    
                 A0 = float(constants_list[1])
                 A1 = float(constants_list[2])
                 A2 = float(constants_list[3])
                 A3 = float(constants_list[4])
                 A4 = float(constants_list[5])
                 A5 = float(constants_list[6])
                 A6 = float(constants_list[7])
                 A7=A8=A9=0
                 
            if length_constants == 7:
                 A0 = float(constants_list[1])
                 A1 = float(constants_list[2])
                 A2 = float(constants_list[3])
                 A3 = float(constants_list[4])
                 A4 = float(constants_list[5])
                 A5 = float(constants_list[6])
                 A6=A7=A8=A9=0
                     
            if length_constants == 6 :
    
                 A0 = float(constants_list[1])
                 A1 = float(constants_list[2])
                 A2 = float(constants_list[3])
                 A3 = float(constants_list[4])
                 A4 = float(constants_list[5])
                 A5=A6=A7=A8=A9=0
                 
            if length_constants == 5:
                 A0 = float(constants_list[1])
                 A1 = float(constants_list[2])
                 A2 = float(constants_list[3])
                 A3 = float(constants_list[4])
                 A4=A5=A6=A7=A8=A9=0
                 
            if length_constants == 4:
    
                 A0 = float(constants_list[1])
                 A1 = float(constants_list[2])
                 A2 = float(constants_list[3])
                 A3=A4=A5=A6=A7=A8=A9=0
                 
            if length_constants == 3:
    
                 A0 = float(constants_list[1])
                 A1 = float(constants_list[2])
                 A2=A3=A4=A5=A6=A7=A8=A9=0
             
            if length_constants == 2:
    
                 A0 = float(constants_list[1])
                 A1=A2=A3=A4=A5=A6=A7=A8=A9=0
        
           
        #else:
              #print('\nThere is no glass with name ' + glass_name + ' in file ' + filename)
            #assigning values 
            D0 = float(temperature_list[1])
            D1 = float(temperature_list[2])
            D2 = float(temperature_list[3])
            E0 = float(temperature_list[4])
            E1 = float(temperature_list[5])
            Ltk = float(temperature_list[6])
            #reference temperature in celcius
            T0 = float(temperature_list[7])
    
            #make the dictionary for all formulas
            formulas_dictionary = {1: 'schott' , 2: 'sellmeier1' , 3: 'sellmeier2' , 4 : 'sellmeier3' , 5 : 'sellmeier4' , 6 : 'sellmeier5', 7 : 'herzberger' , 8 : 'condrady' , 9 : 'handbook_optics1', 10 :'handbook_optics2' , 11 : 'extended1', 12 : 'extended2', 13 : 'extended3' }
        
            #apply loop for find the appropriate formula number and name
            for formulas_number in formulas_dictionary.keys():
                if formulas_number == int(formula_number) :
                    formula_name1 = formulas_dictionary[formulas_number]
                    print('\nFormula name is  :  ' + formula_name1)
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
            n_air_catT0 = (1.0000  +  (((n_air_15 - 1)*101325)/((1.0000 + 0.0034785*(T0 - 15))*101325) ))
                
            #refractive index(air) at temperature T and Pressure P Pa
            n_air_catT = (1.0000  +  (((n_air_15 - 1)*P)/((1.0000 + 0.0034785*(T - 15))*101325) ) )
            print("\nRefractive index of air at given temperature and pressure is : ",end=' ')
            print(n_air_catT)
            
            n_rel_givenT = (n0  +  (n_abs_change/n_air_catT0))*(n_air_catT0/n_air_catT)
     
            print("\nRefractive index at given temperature is : ",end = ' ' )
            print(n_rel_givenT)
            print("Temperature is :  ",end =' ')
            print(T)
        else:
            print('\nThere is no glass with name ' + glass_name + ' in file ' + filename)

if __name__ == "__main__":
    glass_name = input("\nEnter the name of glass type :  ")
    wavelength = float(input("\nEnter the wavelength in nm : "))
    T =float(input("\nEnter the temeperature of surrounding in celcius : "))
    P=float(input("\nEnter the pressure of surrounding in Pa : "))
    thermal_describtion_glass(glass_name,wavelength,P,T)
    
