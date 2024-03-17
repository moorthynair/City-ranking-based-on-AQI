# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:17:51 2021

@author: Moorthy M Nair
"""

import pandas as pd
import requests
from tabula import read_pdf
import numpy as np
import sys

##User Defined Inputs
date = input('Enter the date of analysis in the format YYYYMMDD: ') ## Make sure you call dates on or after 29th January 2018 (20180129)
pathway = input('Define the Pathway address to download the bulletin: ') ##example C:/Users/USER/Downloads
list_of_cities = input('Enter the list of cities seperated by commas and no space: ') ##Example Mumbai,Bangalore,Kolkata. Disclaimer: Make sure the cities mentioned are present in the Bulletin list

############################# Analysis Begins ################################################
## date call check
if date<'20180129':
    sys.exit('You are runing the wrong set of codes. Refer to readme section at https://github.com/moorthynair/City-ranking-based-on-AQI.git')

## Step 1: Download the bulletin
k = requests.get('https://cpcb.nic.in//upload/Downloads/AQI_Bulletin_'+str(date)+'.pdf')

if k.status_code==404:
    sys.exit('No Bulletin exists for the mentioned date. Plese try different date')
 
with open(pathway+'AQI_Bulletin_'+str(date)+'.pdf','wb') as f:
    f.write(k.content)
    
## Step 2: Read the downloaded bulletin file
pathway = pathway+'AQI_Bulletin_'+str(date)+'.pdf'
file = read_pdf(pathway,pages='all')

## Step 3: Concat all the files to common dataframe
new_file = pd.DataFrame()
for i in range (0, len(file)):
    if i%2==0:
        extract_file = file[i]
        new_file = pd.concat([new_file,extract_file], axis=0)
        

## Step 4: Date Cleaning 
##Extract columns names
k= new_file.loc[0, ]
k.reset_index(inplace=True)
column_names = k.loc[1, ]
column_names = column_names[1: ]

## Reset the column names
new_file.columns = column_names

## Drop NA's from the dataframe
new_file.dropna(inplace=True)

## Remove Duplicates and sorty by descending order of Index Value (Index here is AQI)
final_file = new_file.loc[(new_file['City']!='City'), ]
final_file['Index Value']= final_file['Index Value'].astype(int)
final_file.sort_values(by='Index Value',ascending=False, inplace=True)
final_file.reset_index(inplace=True)
final_file.drop(columns=['S.No', 'index'], inplace=True)

## Step 5: Assing the rank based on AQI values
final_file['ranking'] = np.arange(1, len(final_file)+1)

for i in range(0,len(final_file)-1):
    if final_file.loc[i,'Index Value']== final_file.loc[(i+1), 'Index Value']:
        final_file.loc[(i+1), 'ranking']= final_file.loc[i, 'ranking']
        for k in range(i+2,len(final_file)):
            final_file.loc[k, 'ranking'] = final_file.loc[k, 'ranking']-1

final_file ## Final result of analysis for all the cities mentioned in the Bulletin
            
## Step 6: Filter the city as defined by the user
if len(list_of_cities)>0:
    city_list = list_of_cities.split(',')     
    city_ranking = final_file.loc[final_file['City'].isin(city_list), ]

if len(city_ranking)==0:
    sys.exist('No information for the list of cities as inputed are available in the AQI Bulletin')
    
city_ranking ## Final result for list of cities as per the user input
