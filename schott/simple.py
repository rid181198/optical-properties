# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:21:16 2019

@author: crystal
"""

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
    print('Glass name is ' + glass_name)
    #print(words.index(glass_name))
    x=int(words.index(glass_name))
    print('Glass dispersion formula number is ' + words[x+1] + ' and dispersion formula is sellmeier 1')
    

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
         print(j)
         
         with open("c:/schottzemax-20180601.agf") as file:
             lines = file.readlines()
             #display constants for formula
             print(lines[j+3])
        j=j+1
         
    #Total lines
    #print(j)
    
    

            
    
else:
    print('There is no such type of glass in the catalog')    
    

