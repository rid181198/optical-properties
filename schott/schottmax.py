# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:21:16 2019

@author: crystal
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#doing for only one file  "schott"
with open("c:/schottzemax-20180601.agf") as file:
    contents=file.read()
    print(contents)

#another file "ohara"    
#with open("c:/ohara-2018-10-19.agf") as file:
  #  contents=file.read()
   # print(contents)
   
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
    print('Glass dispersion formula number is ' + words[x+1] + ' and dispersion formula is sellmeier 1')
    formula_number=words[x+1]

    #Different formula for different numbers
    #Find the total number of lines and no. of line with specific glass name
    i=0
    j=0
    with open("c:/schottzemax-20180601.agf") as file:
        lines = file.readlines()
    for line in lines:
       # print(line.rstrip())
        if glass_name in line:
         #line number with that glass name
         #print(j)
         
         with open("c:/schottzemax-20180601.agf") as file:
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
    print("\nConstants values for sellmieier 1 are, \nK1 : " + constants_list[1]+'\nL1 : ' + constants_list[2]+ '\nK2 : ' + constants_list[3]+ '\nL2 : ' + constants_list[4] + '\nK3 : ' + constants_list[5]+ '\nL3 : ' + constants_list[6])
    
    #display the validity range
    print("\nWavelength range for validity of the dispersion formula, ")
    print("\nMinimum wavelenth is " + validity_list[1] + ' micrometer ' + 'and Maximum wavelength is  ' + validity_list[2]+' micrometer')
    
    #conversion for range in loop
    x=int(float(validity_list[1])*100000)
    y=int(float(validity_list[2])*100000)
    
    
    #display temperature
    print("\nConstrained temperature is " + temp_list[7]+ ' celcius')
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
    
    V=np.arange(x,y,0.1)
    n = np.sqrt(1.0000000000 + (K1*(V*V/10000000000)/((V*V/10000000000) - L1)) + (K2*(V*V/10000000000)/((V*V/10000000000) - L2)) + (K3*(V*V/10000000000)/((V*V/10000000000) - L3)))  
    X=V/100000
    plt.plot(X,n,'r-')
    plt.xlabel('Wavelength \u03BB (micrometer) ' , fontsize= 14)
    plt.ylabel('Refractive Index n ' , fontsize = 14 )
    #raw data
    #for V in range(x,y,1):
        #n = np.sqrt(1.0000000000 + (K1*(V*V/10000000000)/((V*V/10000000000) - L1)) + (K2*(V*V/10000000000)/((V*V/10000000000) - L2)) + (K3*(V*V/10000000000)/((V*V/10000000000) - L3)))
        #print('\n')
        #print(float(n))   
        
    

    #To find abbe number
    def abbe(V):
        n = np.sqrt(1.0000000000 + (K1*(V*V/10000000000)/((V*V/10000000000) - L1)) + (K2*(V*V/10000000000)/((V*V/10000000000) - L2)) + (K3*(V*V/10000000000)/((V*V/10000000000) - L3)))
        return n   
    nD = abbe(58920)
    nF = abbe(48610)
    nV = abbe(65630)
    #put the values in abbe formula
    abbe1 = (float(nD) -1.0000000)/(float(nF)-float(nV))
    print("\nAbbe number of this glass type is,  " )
    print(float(abbe1))

else:
    print('There is no such type of glass in the catalog')    

