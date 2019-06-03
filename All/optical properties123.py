# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:42:32 2019

@author: crystal
"""
import os
import Formulas as fp

#providing specific glass type by its name i.e. N-SK10
glass_name = input("\nEnter the name of glass type :  ")

#open the directory and files
for filename in os.listdir("c:/AGF"):
    file_string=str(filename)
    
    #open each of the file here file_string is name of the each file
    with open('c:/AGF/'+file_string) as file:
        
        #file_contents_list is list of contents of files
        contents=file.read()
    file_contents_list = contents.split()
        
    #check the condition for name in that list
    if glass_name in file_contents_list :    
         #print the glass name
         print('\nGlass name is in the '+ file_string + ' catalog')
         print('\nGlass name is ' + glass_name)
         
         #find the index of the glass name
         glass_name_index=int(file_contents_list.index(glass_name))
                         
         #find the index of formula number
         formula_number=file_contents_list[glass_name_index+1]
        
         j=0    
         with open('c:/AGF/'+file_string) as file:
                 file_lines_list = file.readlines()
        
         for file_lines in file_lines_list:
             #find the details of the glass
             file_lines_wordlist = file_lines.split()
             if glass_name in file_lines_wordlist :
                 
                 for file_lines in file_lines_list[j:j+20]: 
                 
                    #display constants for formula
                    if 'CD' in file_lines:
                        constants_list = file_lines.split()
                        length = len(constants_list)
            
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
         print("\nAtmosphere temperature is " + temperature_list[7]+ ' celcius')
                 
         
         if length == 11:
    
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

         if length == 10:
    
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

         if length == 9:
    
             A0 = float(constants_list[1])
             A1 = float(constants_list[2])
             A2 = float(constants_list[3])
             A3 = float(constants_list[4])
             A4 = float(constants_list[5])
             A5 = float(constants_list[6])
             A6 = float(constants_list[7])
             A7 = float(constants_list[8])
             A8=A9=0
             
         if length == 8 :
    
             A0 = float(constants_list[1])
             A1 = float(constants_list[2])
             A2 = float(constants_list[3])
             A3 = float(constants_list[4])
             A4 = float(constants_list[5])
             A5 = float(constants_list[6])
             A6 = float(constants_list[7])
             A7=A8=A9=0
    
         if length == 7:
    
             A0 = float(constants_list[1])
             A1 = float(constants_list[2])
             A2 = float(constants_list[3])
             A3 = float(constants_list[4])
             A4 = float(constants_list[5])
             A5 = float(constants_list[6])
             A6=A7=A8=A9=0
             
         if length == 6 :
    
             A0 = float(constants_list[1])
             A1 = float(constants_list[2])
             A2 = float(constants_list[3])
             A3 = float(constants_list[4])
             A4 = float(constants_list[5])
             A5=A6=A7=A8=A9=0
             
         if length == 5:
             A0 = float(constants_list[1])
             A1 = float(constants_list[2])
             A2 = float(constants_list[3])
             A3 = float(constants_list[4])
             A4=A5=A6=A7=A8=A9=0
             
         if length == 4:
    
             A0 = float(constants_list[1])
             A1 = float(constants_list[2])
             A2 = float(constants_list[3])
             A3=A4=A5=A6=A7=A8=A9=0
             
         if length == 3:
    
             A0 = float(constants_list[1])
             A1 = float(constants_list[2])
             A2=A3=A4=A5=A6=A7=A8=A9=0
             
         if length == 2:
    
             A0 = float(constants_list[1])
             A1=A2=A3=A4=A5=A6=A7=A8=A9=0
             
             
         formulas_dictionary = {1: 'schott' , 2: 'sellmeier1' , 3: 'sellmeier2' , 4 : 'sellmeier3' , 5 : 'sellmeier4' , 6 : 'sellmeier5', 7 : 'herzberger' , 8 : 'condrady' , 9 : 'handbook_optics1', 10 :'handbook_optics2' , 11 : 'extended1', 12 : 'extended2', 13 : 'extended3' }
        
         for formulas_number in formulas_dictionary.keys():
             if formulas_number == int(formula_number) :
                 formula_name1 = formulas_dictionary[formulas_number]
                 print('\nFormula name is  :  ' + formula_name1)
                 fp.formula_name(formula_name1,glass_name,formula_number,min_wavelength,max_wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9)
                             
    else:
            print('\nThere is no glass with name ' + glass_name + ' in file ' + filename) 
#save the output in file