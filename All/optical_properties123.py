77# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:42:32 2019

@author: crystal
"""
import os
import Formulas as formula_file
import Thermal_analysis as thermal_file

#providing specific glass type by its name i.e. N-SK10

def optical_describtion_glass(glass_name):
    
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
            
                        #wavelength range list    
                        if 'LD' in file_lines:
                            wavelength_ranges_list = file_lines.split()
                                     
                        #temperature list     
                        if 'TD' in file_lines:
                            temperature_list = file_lines.split()
                            
                j=j+1
                            
            #Total lines
            #print(j)
                            
            #display the validity range
            print("\nWavelength range for validity of the dispersion formula, ")
            print("\nMinimum wavelenth is " + wavelength_ranges_list[1] + ' micrometer ' + 'and Maximum wavelength is  ' + wavelength_ranges_list[2]+' micrometer')
                            
            #defining the validity range for dispersion formula
            min_wavelength=float(wavelength_ranges_list[1])
            max_wavelength=float(wavelength_ranges_list[2])
         
            #print the temperature of that glass
            print("\nReference temperature is " + temperature_list[7]+ ' celcius')
         
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
        
            #make the dictionary for all formulas
            formulas_dictionary = {1: 'schott' , 2: 'sellmeier1' , 3: 'sellmeier2' , 4 : 'sellmeier3' , 5 : 'sellmeier4' , 6 : 'sellmeier5', 7 : 'herzberger' , 8 : 'condrady' , 9 : 'handbook_optics1', 10 :'handbook_optics2' , 11 : 'extended1', 12 : 'extended2', 13 : 'extended3' }
        
            #apply loop for find the appropriate formula number and name
            for formulas_number in formulas_dictionary.keys():
                if formulas_number == int(formula_number) :
                    formula_name1 = formulas_dictionary[formulas_number]
                    print('\nFormula name is  :  ' + formula_name1)
                    formula_file.formula_name(formula_name1,glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            
            #thermal analysis
            thermal_file.thermal_describtion_glass(glass_name,temperature_list,formula_number,formula_name1,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
            #verification
            thermal_file.verification_thermal(glass_name,temperature_list,formula_number,formula_name1,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
        else:
            print('\nThere is no glass with name ' + glass_name + ' in file ' + filename) 

if __name__ == "__main__":
    glass_name = input("\nEnter the name of glass type :  ")
    optical_describtion_glass(glass_name)
    
#save the output in file