# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:42:32 2019

@author: crystal
"""
import numpy as np
import matplotlib.pyplot as plt
import os

#providing condition for specific glass type by its name i.e. N-SK10
glass_name = input("\nEnter the name of glass type :  ")

for filename in os.listdir("c:/AGF"):
    file_string=str(filename)
    with open('c:/AGF/'+file_string) as file:
        contents=file.read()
        #print(contents)
    file_contents_list=contents.split()
    
    
    if glass_name in file_contents_list:
         #with open('c:/AGF/'+file_string) as file:
            # contents=file.read()
             #print(contents)
             #words=contents.split()
             print('\nGlass name is in the '+ file_string + ' catalog')
             #find the index of the that glass name and its data
             print('\nGlass name is ' + glass_name)
             #print(words.index(glass_name))
             x=int(file_contents_list.index(glass_name))
        
             #find the index of formula number
             formula_number=file_contents_list[x+1]
             
             #Different formula for different numbers
             #Find the total number of lines and no. of line with specific glass name
             
             with open('c:/AGF/'+file_string) as file:
                 #file_contents is list
                 file_contents = file.readlines()
             j=0    
             for file_lines in file_contents:
                     # print(line.rstrip())
                     if glass_name in file_lines :
                             #line number with that glass name
                             print('\nGlass name is in the '+ file_string + ' catalog')
                             #find the index of the that glass name and its data
                             print('\nGlass name is ' + glass_name)
                             #print(words.index(glass_name))
                             x=int(file_contents_list.index(glass_name))
                         
                             #find the index of formula number
                             formula_number=file_contents_list[x+1]
                         
                             for file_lines in file_contents[j:j+20]:
                                 #display constants for formula
                                 if 'CD' in file_lines:
                                     constants_list = file_lines.split()
                                     
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
                            
             #conversion for range in loop
             min_wavelength=float(wavelength_ranges_list[1])
             max_wavelength=float(wavelength_ranges_list[2])
                            
                            
             #display temperature
             print("\nAtmosphere temperature is " + temperature_list[7]+ ' celcius')
                            
                            
             #defining function or data set for each formula
             def sellmeier1():
                                
                                 print('\nGlass dispersion formula number is ' + formula_number + ' and dispersion formula is sellmeier 1')
                                
                                 print("\nConstants values for sellmieier 1 are, \nK1 : " + constants_list[1]+'\nL1 : ' + constants_list[2]+ '\nK2 : ' + constants_list[3]+ '\nL2 : ' + constants_list[4] + '\nK3 : ' + constants_list[5]+ '\nL3 : ' + constants_list[6])
                                 #formula for refractive index
                                 #K1,K2,K3,L1,L2,L3 are constant of formula
                                 #n is refractive index
                                 #V is wavelength of light
                                 K1 = float(constants_list[1])
                                 L1 = float(constants_list[2])
                                 K2 = float(constants_list[3])
                                 L2 = float(constants_list[4])
                                 K3 = float(constants_list[5])
                                 L3 = float(constants_list[6])
                                
                                 #plot refractive index vs wavelength    
                                 wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
                                 n = np.sqrt(1.0000000000 + (K1*(wavelength*wavelength)/(wavelength*wavelength - L1)) + (K2*wavelength*wavelength/(wavelength*wavelength - L2)) + (K3*wavelength*wavelength/(wavelength*wavelength - L3)))  
                                 X=wavelength*1000
                                 plt.plot(X,n,'r-')
                                 plt.xlabel('Wavelength \u03BB (nm) ' , fontsize= 14)
                                 plt.ylabel('Refractive Index n ' , fontsize = 14 )
                                 
                                 #raw data
                                 #for V in range(x,y,1):
                                 #n = np.sqrt(1.0000000000 + (K1*(V*V/10000000000)/((V*V/10000000000) - L1)) + (K2*(V*V/10000000000)/((V*V/10000000000) - L2)) + (K3*(V*V/10000000000)/((V*V/10000000000) - L3)))
                                 #print('\n')
                                 #print(float(n))   
                                 
                                 #To find abbe number
             def abbe_sellmeier1(wavelength):
                                     K1 = float(constants_list[1])
                                     L1 = float(constants_list[2])
                                     K2 = float(constants_list[3])
                                     L2 = float(constants_list[4])
                                     K3 = float(constants_list[5])
                                     L3 = float(constants_list[6])
                                     n = np.sqrt(1.0000000000 + (K1*(wavelength*wavelength)/(wavelength*wavelength - L1)) + (K2*wavelength*wavelength/(wavelength*wavelength - L2)) + (K3*wavelength*wavelength/(wavelength*wavelength - L3)))
                                     return n   
                                 
                                 
                                 #Data set for schott formula   
             def schott():
                                      print('\nGlass dispersion formula number is ' + formula_number + ' and dispersion formula is schott')      
                                     
                                      print("\nConstants values for schott are, \nA0 : " + constants_list[1]+'\nA1 : ' + constants_list[2]+ '\nA2 : ' + constants_list[3]+ '\nA3 : ' + constants_list[4] + '\nA4 : ' + constants_list[5]+ '\nA5 : ' + constants_list[6])
                                      #formula for refractive index
                                      #A0,A1,A2,A3,A4,A5 are constant of formula
                                      #n is refractive index
                                      #V is wavelength of light in micrometer
                                      A0 = float(constants_list[1])
                                      A1 = float(constants_list[2])
                                      A2 = float(constants_list[3])
                                      A3 = float(constants_list[4])
                                      A4 = float(constants_list[5])
                                      A5 = float(constants_list[6])
                                     
                                      wavelength=np.arange(min_wavelength,max_wavelength,0.0001)
                                      n=((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
                                      X=wavelength*1000
                                      plt.plot(X,n,'r-')
                                      plt.xlabel('Wavelength \u03BB (nm) ' , fontsize= 14)
                                      plt.ylabel('Refractive Index n ' , fontsize = 14 )
                                      #raw data
                                      #for V in range(x,y):
                                      #n = np.sqrt(A0 + (A1*((V*V)/10000000000)) + (A2*(10000000000/(V*V))) + (A3*(100000000000000000000/(V*V*V*V))) + (A4*(1000000000000000000000000000000/(V*V*V*V*V*V))) + (A5*(10000000000000000000000000000000000000000/(V*V*V*V*V*V*V*V))))
                                      #print('\n')
                                      #print(float(n))  
                                    
                                      #To find abbe number
             def abbe_schott(wavelength):
                                        A0 = float(constants_list[1])
                                        A1 = float(constants_list[2])
                                        A2 = float(constants_list[3])
                                        A3 = float(constants_list[4])
                                        A4 = float(constants_list[5])
                                        A5 = float(constants_list[6])
                                        n=((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
                                        return n   
                                    
             #formula 1(schott)
             if formula_number == '1' :
                                        #calling function
                                        schott()
                                        
                                        nD = abbe_schott(0.58920)
                                        nF = abbe_schott(0.48610)
                                        nV = abbe_schott(0.65630)
                                        
                                        #put the values in abbe formula
                                        abbe1 = (float(nD) -1.0000000)/(float(nF)-float(nV))
                                        print("\nAbbe number of this glass type is,  " )
                                        print(float(abbe1))
                                        get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
                                        if get_refractive_index == 'y':
                                            wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
                                            wavelength = float(wavelength)/1000
                                            A0 = float(constants_list[1])
                                            A1 = float(constants_list[2])
                                            A2 = float(constants_list[3])
                                            A3 = float(constants_list[4])
                                            A4 = float(constants_list[5])
                                            A5 = float(constants_list[6])
                                            n=((A0) + (A1*(wavelength*wavelength)) + (A2/(wavelength*wavelength)) + (A3/(wavelength*wavelength*wavelength*wavelength)) + (A4/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)) + (A5/(wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength*wavelength)))**(1/2)
                                            print(n)
                                        else:
                                            break 
                                            
                                            
                                        
                                        
                                        #formula 2(sellmeier)     
             elif formula_number == '2':
                                            #calling function
                                            sellmeier1()    
                                            
                                            nD = abbe_sellmeier1(0.58920)
                                            nF = abbe_sellmeier1(0.48610)
                                            nV = abbe_sellmeier1(0.65630)
                                            
                                            #put the values in abbe formula
                                            abbe1 = (float(nD) -1.0000000)/(float(nF)-float(nV))
                                            print("\nAbbe number of this glass type is,  " )
                                            print(float(abbe1))
                                            get_refractive_index = input("\nDo you want to get refractive index of specific wavelength (y/n) :  " )
                                            if get_refractive_index == 'y':
                                                wavelength = input("\n\n Please enter the wavelength in nanometer :  ")
                                                wavelength = float(wavelength)/1000
                                                K1 = float(constants_list[1])
                                                L1 = float(constants_list[2])
                                                K2 = float(constants_list[3])
                                                L2 = float(constants_list[4])
                                                K3 = float(constants_list[5])
                                                L3 = float(constants_list[6])
                                                n = np.sqrt(1.0000000000 + (K1*(wavelength*wavelength)/(wavelength*wavelength - L1)) + (K2*wavelength*wavelength/(wavelength*wavelength - L2)) + (K3*wavelength*wavelength/(wavelength*wavelength - L3))) 
                                                print(n)
                                            else:
                                                break 
                                            
    else:
        print('\nThere is no glass with name ' + glass_name + ' in file ' + filename)
        
#save the output in file