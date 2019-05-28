# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:21:16 2019

@author: crystal
"""
import numpy as np
import matplotlib.pyplot as plt

#doing for only one file  "ohara"
with open("c:/ohara-2018-10-19.agf") as file:
    contents=file.read()
    print(contents)

#splitting file into words or making list   
words=contents.split()
#print(words)

#providing condition for specific glass type by its name i.e. N-SK10
glass_name = input("Enter the exact name of glass :  ")
if glass_name in words:
    print('Glass name is in the catalog')
    
    #find the index of the that glass name and its data
    print('\nGlass name is ' + glass_name)
    #print(words.index(glass_name))
    x=int(words.index(glass_name))
    print('Glass dispersion formula number is ' + words[x+1] + ' and dispersion formula is schott')
    formula_number=words[x+1]

    #Different formula for different numbers
    #Find the total number of lines and no. of line with specific glass name
    i=0
    j=0
    with open("c:/ohara-2018-10-19.agf") as file:
        lines = file.readlines()
    for line in lines:
       # print(line.rstrip())
        if glass_name in line:
         #line number with that glass name
         #print(j)
         
         with open("c:/ohara-2018-10-19.agf") as file:
             lines = file.readlines()
             #display constants for formula
             constants = lines[j+3]
             #print(constants)
             
             #formula validity within that range
             validity_range = lines[j+6]
             #print(validity_range)
             validity_list = validity_range.split()
             
             #for temperature
             temp=lines[j+4]
             temp_list=temp.split()
        j=j+1
         
    #Total lines
    #print(j)
    
    #display constants values
    constants_list=constants.split()
    print("\nConstants values for schott are, \nA0 : " + constants_list[1]+'\nA1 : ' + constants_list[2]+ '\nA2 : ' + constants_list[3]+ '\nA3 : ' + constants_list[4] + '\nA4 : ' + constants_list[5]+ '\nA5 : ' + constants_list[6])
    
    #display the validity range
    print("\nWavelength range for validity of the dispersion formula, ")
    print("\nMinimum wavelenth is " + validity_list[1] + ' micrometer ' + 'and Maximum wavelength is  ' + validity_list[2]+' micrometer')
    
    #conversion for range in loop
    x=int(float(validity_list[1])*100000)
    y=int(float(validity_list[2])*100000)
    
    
    #display temperature
    print("\nConstrained temperature is " + temp_list[7]+ ' celcius')
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
    
    V=np.arange(x,y,0.1)
    n = (A0 + (A1*((V*V)/10000000000)) + (A2*(10000000000/(V*V))) + (A3*(100000000000000000000/(V*V*V*V))) + (A4*(1000000000000000000000000000000/(V*V*V*V*V*V))) + (A5*(10000000000000000000000000000000000000000/(V*V*V*V*V*V*V*V))))**1/2    
    X=V/100000
    plt.plot(X,n,'r-')
    #raw data
    #for V in range(x,y):
        #n = (A0 + (A1*((V*V)/10000000000)) + (A2*(10000000000/(V*V))) + (A3*(100000000000000000000/(V*V*V*V))) + (A4*(1000000000000000000000000000000/(V*V*V*V*V*V))) + (A5*(10000000000000000000000000000000000000000/(V*V*V*V*V*V*V*V))))**1/2    
        #print('\n')
        #print(float(n))   
       
else:
    print('There is no such type of glass in the catalog')    

