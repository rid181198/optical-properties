# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:20:19 2019

@author: crystal
"""
import Formulas as formula_file
import os
from prettytable import PrettyTable
from urllib.request import urlopen
from bs4 import BeautifulSoup

url_g='https://refractiveindex.info/?shelf=glass&book=BK7&page=SCHOTT'
html = urlopen(url_g)
soup = BeautifulSoup(html, 'lxml')

#for glass catalog
opt_group = soup.find_all('optgroup')
print("Please select the catalog book for validation from below list and enter option value attribute")

for i in range(len(opt_group)):
    print("\n")
    print(opt_group[i])
 
glass_catalog = input("Enter the name of glass catalog :  ")

#for glass name
url1_c = 'https://refractiveindex.info/?shelf=glass&book='
url2_c = glass_catalog
url3_c = '&page='

html = urlopen(url1_c + url2_c + url3_c)
soup = BeautifulSoup(html,'lxml')

select_page = soup.find_all('select',id = 'page')
print("\nPlease select the glass name for validation from below list and enter option value attribute")
print(select_page)

glass_name = input("Enter the the glass name from list : ")

#open the specific link
url = 'https://refractiveindex.info/?shelf=glass&book='
url2 = str(glass_catalog)
url3 = '&page='
url4 = str(glass_name)
html = urlopen(url+url2+url3+url4)
soup = BeautifulSoup(html, 'lxml')
    
#split the script data
script = soup.find_all('script')
data_script = str(script[7])
new_data1 = data_script.replace('[',' ')
new_data2 = new_data1.replace(']',' ')
data_split = new_data2.split()
    
#data for wavelengths
index1 = int(data_split.index('data_n_wl='))
data_n_wl = data_split[index1 +1]
#print(data_n_wl)
    
#data for refractive index
index2 = int(data_split.index('data_n='))
#print('\n')
data_n = data_split[index2 + 1]
#print(data_n)
    
#make list and represent with float number (for wavelengths and refractive index)
n_wl_split = data_n_wl.split(',')
n_split = data_n.split(',')
#loop and print the table
print("   Wavelengths micrometer       Refractive index  " )
for i in range(len(n_wl_split)):
    table = PrettyTable(['Wavelength', 'Refractive index in the webpage'])
    table.add_row([float(n_wl_split[i]),float(n_split[i])])
    print(table)
        




#open the directory and files
#calculated refractive index
glass_name = input("\nEnter the name of glass type :  ")  
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
        
        formulas_dictionary = {1: 'schott' , 2: 'sellmeier1' , 3: 'sellmeier2' , 4 : 'sellmeier3' , 5 : 'sellmeier4' , 6 : 'sellmeier5', 7 : 'herzberger' , 8 : 'condrady' , 9 : 'handbook_optics1', 10 :'handbook_optics2' , 11 : 'extended1', 12 : 'extended2', 13 : 'extended3' }
        
        #apply loop for find the appropriate formula number and name
        for formulas_number in formulas_dictionary.keys():
            if formulas_number == int(formula_number) :
                formula_name1 = formulas_dictionary[formulas_number]
                for wavelength in n_wl_split:
                    wavelength = float(wavelength)
                    RI = float(formula_file.formula_thermal_name(formula_name1,wavelength,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9))
                    table = PrettyTable(['Wavelength', 'Refractive index calculated'])
                    table.add_row([float(wavelength),RI])
                    print(table)
    else:
            print('\nThere is no glass with name ' + glass_name + ' in file ' + filename)             




        