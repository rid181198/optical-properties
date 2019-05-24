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
else:
    print('There is no such type of glass in the catalog')    
    
#find the index of the that glass name and its data
print('Glass name is ' + glass_name)
#print(words.index(glass_name))
x=int(words.index(glass_name))
print('Glass dispersion formula number is ' + words[x+1])

#Different formula for different numbers

