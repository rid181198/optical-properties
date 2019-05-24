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
    print(words.index('N-SK10'))
    print(words[19581])
else:
    print('There is no such type of glass in the catalog')    
    
