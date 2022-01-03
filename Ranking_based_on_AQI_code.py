# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:17:51 2021

@author: HP
"""

import pandas as pd
import openaq
import datetime
from tabula import read_pdf
import numpy as np
import os

##Input the file
pathway = 'C:/Users/HP/Downloads/AQI_Bulletin_20211231.pdf'
file = read_pdf(pathway,pages='all')


new_file = pd.DataFrame()
##Concat all the files to common dataframe
for i in range (0, len(file)):
    if i%2==0:
        extract_file = file[i]
        new_file = pd.concat([new_file,extract_file], axis=0)
        

##Extract columns names
k= new_file.loc[0, ]
k.reset_index(inplace=True)
column_names = k.loc[1, ]
column_names = column_names[1: ]

## Reset the columns
new_file.columns = column_names

##Drop NA's from new_file
new_file.dropna(inplace=True)

final_file = new_file.loc[(new_file['City']!='City'), ]
final_file['Index Value']= final_file['Index Value'].astype(int)
final_file.sort_values(by='Index Value',ascending=False, inplace=True)
final_file.reset_index(inplace=True)
final_file.drop(columns=['S.No', 'index'], inplace=True)
final_file['ranking'] = np.arange(1, len(final_file)+1)
final_file['of Monitoring']= final_file['of Monitoring'].astype('int')

for i in range(0,len(final_file)-1):
    if final_file.loc[i,'Index Value']== final_file.loc[(i+1), 'Index Value']:
        final_file.loc[(i+1), 'ranking']= final_file.loc[i, 'ranking']
        for k in range(i+2,len(final_file)):
            final_file.loc[k, 'ranking'] = final_file.loc[k, 'ranking']-1

city_list = ['Bettiah','Bhagalpur','Bihar Sharif','Buxar','Chhapra','Darbhanga','Gaya','Hajipur',
             'Katihar','Kishanganj','Manguraha','Motihari','Munger','Muzaffarpur','Patna','Purnia',
             'Rajgir','Saharsa','Sasaram','Siwan']        
city_ranking = final_file.loc[final_file['City'].isin(city_list), ]






