# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:21:16 2019

@author: crystal
"""
import numpy as np
import matplotlib.pyplot as plt

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
    
    #find the index of formula number
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
    
    #display the validity range
    print("\nWavelength range for validity of the dispersion formula, ")
    print("\nMinimum wavelenth is " + validity_list[1] + ' micrometer ' + 'and Maximum wavelength is  ' + validity_list[2]+' micrometer')
    
    #conversion for range in loop
    x=int(float(validity_list[1])*100000)
    y=int(float(validity_list[2])*100000)
    
    
    #display temperature
    print("\nAtmosphere temperature is " + temp_list[7]+ ' celcius')
    
    
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
    def abbe_sellmeier1(V):
        K1 = float(constants_list[1])
        L1 = float(constants_list[2])
        K2 = float(constants_list[3])
        L2 = float(constants_list[4])
        K3 = float(constants_list[5])
        L3 = float(constants_list[6])
        n = np.sqrt(1.0000000000 + (K1*(V*V/10000000000)/((V*V/10000000000) - L1)) + (K2*(V*V/10000000000)/((V*V/10000000000) - L2)) + (K3*(V*V/10000000000)/((V*V/10000000000) - L3)))
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
    
          V=np.arange(x,y,0.1)
          n=((A0) + (A1*((V*V)/10000000000)) + (A2*(10000000000/(V*V))) + (A3*(100000000000000000000/(V*V*V*V))) + (A4*(1000000000000000000000000000000/(V*V*V*V*V*V))) + (A5*(10000000000000000000000000000000000000000/(V*V*V*V*V*V*V*V))))**(1/2)
          X=V/100000
          plt.plot(X,n,'r-')
          plt.xlabel('Wavelength \u03BB (micrometer) ' , fontsize= 14)
          plt.ylabel('Refractive Index n ' , fontsize = 14 )
          #raw data
          #for V in range(x,y):
              #n = np.sqrt(A0 + (A1*((V*V)/10000000000)) + (A2*(10000000000/(V*V))) + (A3*(100000000000000000000/(V*V*V*V))) + (A4*(1000000000000000000000000000000/(V*V*V*V*V*V))) + (A5*(10000000000000000000000000000000000000000/(V*V*V*V*V*V*V*V))))
              #print('\n')
              #print(float(n))  
        
    #To find abbe number
    def abbe_schott(V):
        A0 = float(constants_list[1])
        A1 = float(constants_list[2])
        A2 = float(constants_list[3])
        A3 = float(constants_list[4])
        A4 = float(constants_list[5])
        A5 = float(constants_list[6])
        n = np.sqrt((A0 + (A1*((V*V)/10000000000)) + (A2*(10000000000/(V*V))) + (A3*(100000000000000000000/(V*V*V*V))) + (A4*(1000000000000000000000000000000/(V*V*V*V*V*V))) + (A5*(10000000000000000000000000000000000000000/(V*V*V*V*V*V*V*V)))))
        return n   
         
    #formula 1(schott)
    if formula_number == '1' :
         #calling function
         schott()
         
         nD = abbe_schott(58920)
         nF = abbe_schott(48610)
         nV = abbe_schott(65630)
         
         #put the values in abbe formula
         abbe1 = (float(nD) -1.0000000)/(float(nF)-float(nV))
         print("\nAbbe number of this glass type is,  " )
         print(float(abbe1))
         
         
    #formula 2(sellmeier)     
    elif formula_number == '2':
         #calling function
         sellmeier1()    
         
         nD = abbe_sellmeier1(58920)
         nF = abbe_sellmeier1(48610)
         nV = abbe_sellmeier1(65630)
         
         #put the values in abbe formula
         abbe1 = (float(nD) -1.0000000)/(float(nF)-float(nV))
         print("\nAbbe number of this glass type is,  " )
         print(float(abbe1))
            
else:
    print('There is no such type of glass in the catalog')    