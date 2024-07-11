# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:37:07 2024

@author: Eleni
Collect data from DAM, CRIDAs and XBID
Prices and volumes traded
"""

"""
Libraries
"""

import os
import pandas as pd
from datetime import datetime, timedelta
import re

"""
DAM
Loop collect the data
"""

"""
2024
To be completed
"""
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 DAM"

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 31)
date_format = "%Y%m%d"
current_date = start_date

df = pd.DataFrame()
while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    file_name = f"{date_str}_EL-DAM_PrelimResults_EN_v01.xls"
    file_path = os.path.join(base_directory, file_name)
    file_path = re.sub(r'\\', '/', file_path)
    df1 = pd.read_excel(file_path)
    trades = df1.groupby(['DELIVERY_MTU','ASSET_DESCR', 'CLASSIFICATION','MCP'])['TOTAL_TRADES'].sum().reset_index()
    trades.set_index('DELIVERY_MTU')
    df = pd.concat([df, trades], axis = 0)
    current_date += timedelta(days=1)
df.head()
df.drop(['CLASSIFICATION','ASSET_DESCR'], axis = 1, inplace = True)
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
df['Month'] = df['DELIVERY_MTU'].dt.to_period('M')
grouped_df = df.groupby('Month')['TOTAL_TRADES'].sum().reset_index()
grouped_df['Total Traded GW'] = grouped_df['TOTAL_TRADES']/1000

df.set_index('DELIVERY_MTU', inplace=True)

path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\DAM\2024.xlsx"
path = path.replace('\\','/')
df.to_excel(path) 

"""
Do the same but keep only tradded volumes and MCP
"""
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\2024 DAM"

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 4, 3)
date_format = "%Y%m%d"
current_date = start_date

df = pd.DataFrame()
while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    file_name = f"{date_str}_EL-DAM_PrelimResults_EN_v01.xls"
    file_path = os.path.join(base_directory, file_name)
    file_path = re.sub(r'\\', '/', file_path)
    df1 = pd.read_excel(file_path)
    trades = df1.groupby(['DELIVERY_MTU','MCP'])['TOTAL_TRADES'].sum().reset_index()
    trades.set_index('DELIVERY_MTU')
    df = pd.concat([df, trades], axis = 0)
    current_date += timedelta(days=1)

df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
df.set_index('DELIVERY_MTU', inplace=True)
df.head()
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\DAM\CORE 2024.xlsx"
path = path.replace('\\','/')
df.to_excel(path) 
"""
2023
"""
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2023 DAM"

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_format = "%Y%m%d"
current_date = start_date

df = pd.DataFrame()
while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    file_name = f"{date_str}_EL-DAM_Results_EN_v01.xlsx"
    file_path = os.path.join(base_directory, file_name)
    file_path = re.sub(r'\\', '/', file_path)
    df1 = pd.read_excel(file_path)
    trades = df1.groupby(['DELIVERY_MTU','ASSET_DESCR', 'CLASSIFICATION','MCP'])['TOTAL_TRADES'].sum().reset_index()
    trades.set_index('DELIVERY_MTU')
    df = pd.concat([df, trades], axis = 0)
    current_date += timedelta(days=1)

df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
df.info()
result = df.groupby('DELIVERY_MTU').agg({
    'TOTAL_TRADES': 'sum',
    'MCP': 'first'
}).reset_index()
result.info()

result.set_index('DELIVERY_MTU', inplace=True)

path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\DAM\2023.xlsx"
path = path.replace('\\','/')
result.to_excel(path)


"""
2022
"""
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2022_EL-DAM-CRIDAs_Results\2022_EL-DAM_Results"
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
date_format = "%Y%m%d"
current_date = start_date

df = pd.DataFrame()
while current_date <= end_date:
    date_str = current_date.strftime(date_format)
    file_name = f"{date_str}_EL-DAM_Results_EN_v01.xlsx"
    file_path = os.path.join(base_directory, file_name)
    file_path = re.sub(r'\\', '/', file_path)
    df1 = pd.read_excel(file_path)
    trades = df1.groupby(['DELIVERY_MTU','MCP'])['TOTAL_TRADES'].sum().reset_index()
    trades.set_index('DELIVERY_MTU')
    df = pd.concat([df, trades], axis = 0)
    current_date += timedelta(days=1)

df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
#df.set_index('DELIVERY_MTU', inplace=True)
result = df.groupby('DELIVERY_MTU').agg({
    'TOTAL_TRADES': 'sum',
    'MCP': 'first'
}).reset_index()
result.info()

result.set_index('DELIVERY_MTU', inplace=True)

path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\DAM\CORE 2022.xlsx"
path = path.replace('\\','/')
result.to_excel(path) 



"""
Create the CORE 2021 ONLY
"""
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2021_EL-DAM-CRIDAs_PrelimResults\2021_EL-DAM_PrelimResults"
start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 12, 31)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
while current_date <= end_date:
    for version in range(1, 5):  # Iterate over versions v01 to v04
        date_str = current_date.strftime(date_format)
        file_name = f"{date_str}_EL-DAM_PrelimResults_EN_v{version:02d}.xlsx"  # Format the file name
        file_path = os.path.join(base_directory, file_name)
        file_path = re.sub(r'\\', '/', file_path)
        
        if os.path.exists(file_path):  # Check if the file exists
            df1 = pd.read_excel(file_path, sheet_name='SITE_BZ_NP_PRICES')
            trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['NET_POSITION'].sum().reset_index()
            df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
  
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
df.info()
#df.set_index('DELIVERY_MTU', inplace=True)
result = df.groupby('DELIVERY_MTU').agg({
    'NET_POSITION': 'sum',
    'MCP': 'first'
}).reset_index()
result.info()

result.set_index('DELIVERY_MTU', inplace=True)    
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\DAM\CORE 2021.xlsx"
path = path.replace('\\','/')
result.to_excel(path)       
##########################################################################################################################################################################    

"""
CRIDA 1
Loop collect the data
ONLY CORE COLLECTION
"""
#2024
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 CRIDA\CRIDA 1"
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 4, 3)
date_format = "%Y%m%d"
current_date = start_date

df = pd.DataFrame()
while current_date <= end_date:
    
    date_str = current_date.strftime(date_format)
    file_name = f"{date_str}_EL-CRIDA1.xlsx"  # Format the file name
    file_path = os.path.join(base_directory, file_name)
    file_path = re.sub(r'\\', '/', file_path)
        
    if os.path.exists(file_path):  # Check if the file exists
        df1 = pd.read_excel(file_path, sheet_name='SITE_BZ_NP_PRICES')
        trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['NET_POSITION'].sum().reset_index()
        df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
df.info()
result = df.groupby('DELIVERY_MTU').agg({
    'NET_POSITION': 'sum',
    'MCP': 'first'
}).reset_index()
    
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\CRIDA 1\CORE 2024.xlsx"
path = path.replace('\\','/')
result.to_excel(path)       

#2023
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2023 CRIDA\CRIDA 1"
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
while current_date <= end_date:
    
    date_str = current_date.strftime(date_format)
    file_name = f"{date_str}_EL-CRIDA1.xlsx"  # Format the file name
    file_path = os.path.join(base_directory, file_name)
    file_path = re.sub(r'\\', '/', file_path)
        
    if os.path.exists(file_path):  # Check if the file exists
        df1 = pd.read_excel(file_path, sheet_name='SITE_BZ_NP_PRICES')
        trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['NET_POSITION'].sum().reset_index()
        df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
#df.set_index('DELIVERY_MTU', inplace=True)
result = df.groupby('DELIVERY_MTU').agg({
    'NET_POSITION': 'sum',
    'MCP': 'first'
}).reset_index()
        
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\CRIDA 1\CORE 2023.xlsx"
path = path.replace('\\','/')
result.to_excel(path)                 
 
#2022
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2022_EL-DAM-CRIDAs_Results\2022_EL-CRIDA1_Results"
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
while current_date <= end_date:
    for version in range(1, 5):  # Iterate over versions v01 to v04
        date_str = current_date.strftime(date_format)
        file_name = f"{date_str}_EL-CRIDA1_Results_EN_v{version:02d}.xlsx"  # Format the file name
        file_path = os.path.join(base_directory, file_name)
        file_path = re.sub(r'\\', '/', file_path)
        
        if os.path.exists(file_path):  # Check if the file exists
            df1 = pd.read_excel(file_path)
            trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['TOTAL_TRADES'].sum().reset_index()
            df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
  
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
df.info()
result = df.groupby('DELIVERY_MTU').agg({
    'TOTAL_TRADES': 'sum',
    'MCP': 'first'
}).reset_index()
        
    
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\CRIDA 1\CORE 2022.xlsx"
path = path.replace('\\','/')
result.to_excel(path)        

#2021
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2021_EL-DAM-CRIDAs_PrelimResults\2021_EL-CRIDA1-PrelimResults"
start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 12, 31)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
while current_date <= end_date:
    for version in range(1, 5):  # Iterate over versions v01 to v04
        date_str = current_date.strftime(date_format)
        file_name = f"{date_str}_EL-CRIDA1_PrelimResults_EN_v{version:02d}.xlsx"  # Format the file name
        file_path = os.path.join(base_directory, file_name)
        file_path = re.sub(r'\\', '/', file_path)
        
        if os.path.exists(file_path):  # Check if the file exists
            df1 = pd.read_excel(file_path, sheet_name='SITE_BZ_NP_PRICES')
            trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['NET_POSITION'].sum().reset_index()
            df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
  
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
result = df.groupby('DELIVERY_MTU').agg({
    'NET_POSITION': 'sum',
    'MCP': 'first'
}).reset_index()
    
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\CRIDA 1\CORE 2021.xlsx"
path = path.replace('\\','/')
result.to_excel(path)
###########################################################################################################################################################################
"""
CRIDA 2
Loop collect the data
ONLY CORE COLLECTION
"""
#2024
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 CRIDA\CRIDA 2"
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 4, 3)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
while current_date <= end_date:
    
    date_str = current_date.strftime(date_format)
    file_name = f"{date_str}_EL-CRIDA2.xlsx"  # Format the file name
    file_path = os.path.join(base_directory, file_name)
    file_path = re.sub(r'\\', '/', file_path)
        
    if os.path.exists(file_path):  # Check if the file exists
        df1 = pd.read_excel(file_path, sheet_name='SITE_BZ_NP_PRICES')
        trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['NET_POSITION'].sum().reset_index()
        df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
  
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
#df.set_index('DELIVERY_MTU', inplace=True)
df.info()   
result = df.groupby('DELIVERY_MTU').agg({
    'NET_POSITION': 'sum',
    'MCP': 'first'
}).reset_index() 
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\CRIDA 2\CORE 2024.xlsx"
path = path.replace('\\','/')
result.to_excel(path)        

#2023
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2023 CRIDA\CRIDA 2"
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
while current_date <= end_date:

    date_str = current_date.strftime(date_format)
    file_name = f"{date_str}_EL-CRIDA2.xlsx"  # Format the file name
    file_path = os.path.join(base_directory, file_name)
    file_path = re.sub(r'\\', '/', file_path)
        
    if os.path.exists(file_path):  # Check if the file exists
        df1 = pd.read_excel(file_path, sheet_name='SITE_BZ_NP_PRICES')
        trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['NET_POSITION'].sum().reset_index()
        df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
  
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
#df.set_index('DELIVERY_MTU', inplace=True)
df.info()   
result = df.groupby('DELIVERY_MTU').agg({
    'NET_POSITION': 'sum',
    'MCP': 'first'
}).reset_index()     
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\CRIDA 2\CORE 2023.xlsx"
path = path.replace('\\','/')
result.to_excel(path)         
 
#2022
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2022_EL-DAM-CRIDAs_Results\2022_EL-CRIDA2_Results"
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
while current_date <= end_date:
    for version in range(1, 5):  # Iterate over versions v01 to v04
        date_str = current_date.strftime(date_format)
        file_name = f"{date_str}_EL-CRIDA2_Results_EN_v{version:02d}.xlsx"  # Format the file name
        file_path = os.path.join(base_directory, file_name)
        file_path = re.sub(r'\\', '/', file_path)
        
        if os.path.exists(file_path):  # Check if the file exists
            df1 = pd.read_excel(file_path)
            trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['TOTAL_TRADES'].sum().reset_index()
            df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
  
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
df.info()
result = df.groupby('DELIVERY_MTU').agg({
    'TOTAL_TRADES': 'sum',
    'MCP': 'first'
}).reset_index()         
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\CRIDA 2\CORE 2022.xlsx"
path = path.replace('\\','/')
result.to_excel(path)        

#2021
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2021_EL-DAM-CRIDAs_PrelimResults\2021_EL-CRIDA2_PrelimResults"
start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 12, 31)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
while current_date <= end_date:
    for version in range(1, 5):  # Iterate over versions v01 to v04
        date_str = current_date.strftime(date_format)
        file_name = f"{date_str}_EL-CRIDA2_PrelimResults_EN_v{version:02d}.xlsx"  # Format the file name
        file_path = os.path.join(base_directory, file_name)
        file_path = re.sub(r'\\', '/', file_path)
        
        if os.path.exists(file_path):  # Check if the file exists
            df1 = pd.read_excel(file_path, sheet_name='SITE_BZ_NP_PRICES')
            trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['NET_POSITION'].sum().reset_index()
            df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
  
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
df.info()
result = df.groupby('DELIVERY_MTU').agg({
    'NET_POSITION': 'sum',
    'MCP': 'first'
}).reset_index()      
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\CRIDA 2\CORE 2021.xlsx"
path = path.replace('\\','/')
result.to_excel(path)

"""
CRIDA 3
Loop collect the data
ONLY CORE COLLECTION
"""
#2024
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 CRIDA\CRIDA 3"
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 4, 3)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
while current_date <= end_date:
    
    date_str = current_date.strftime(date_format)
    file_name = f"{date_str}_EL-CRIDA3.xlsx"  # Format the file name
    file_path = os.path.join(base_directory, file_name)
    file_path = re.sub(r'\\', '/', file_path)
        
    if os.path.exists(file_path):  # Check if the file exists
        df1 = pd.read_excel(file_path, sheet_name='SITE_BZ_NP_PRICES')
        trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['NET_POSITION'].sum().reset_index()
        df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
  
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
df.info()
result = df.groupby('DELIVERY_MTU').agg({
    'NET_POSITION': 'sum',
    'MCP': 'first'
}).reset_index()      
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\CRIDA 3\CORE 2024.xlsx"
path = path.replace('\\','/')
result.to_excel(path)       

#2023
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2023 CRIDA\CRIDA 3"
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
while current_date <= end_date:
    
    date_str = current_date.strftime(date_format)
    file_name = f"{date_str}_EL-CRIDA3.xlsx"  # Format the file name
    file_path = os.path.join(base_directory, file_name)
    file_path = re.sub(r'\\', '/', file_path)
        
    if os.path.exists(file_path):  # Check if the file exists
        df1 = pd.read_excel(file_path, sheet_name='SITE_BZ_NP_PRICES')
        trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['NET_POSITION'].sum().reset_index()
        df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
  
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
df.info()
result = df.groupby('DELIVERY_MTU').agg({
    'NET_POSITION': 'sum',
    'MCP': 'first'
}).reset_index()   
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\CRIDA 3\CORE 2023.xlsx"
path = path.replace('\\','/')
result.to_excel(path)          
 
#2022
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2022_EL-DAM-CRIDAs_Results\2022_EL-CRIDA3_Results"
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
while current_date <= end_date:
    for version in range(1, 5):  # Iterate over versions v01 to v04
        date_str = current_date.strftime(date_format)
        file_name = f"{date_str}_EL-CRIDA3_Results_EN_v{version:02d}.xlsx"  # Format the file name
        file_path = os.path.join(base_directory, file_name)
        file_path = re.sub(r'\\', '/', file_path)
        
        if os.path.exists(file_path):  # Check if the file exists
            df1 = pd.read_excel(file_path)
            trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['TOTAL_TRADES'].sum().reset_index()
            df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
  
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
df.info()
result = df.groupby('DELIVERY_MTU').agg({
    'TOTAL_TRADES': 'sum',
    'MCP': 'first'
}).reset_index()  
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\CRIDA 3\CORE 2022.xlsx"
path = path.replace('\\','/')
result.to_excel(path)        
   

#2021
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2021_EL-DAM-CRIDAs_PrelimResults\2021_EL-CRIDA3_PrelimResults"
start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 12, 31)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
while current_date <= end_date:
    for version in range(1, 5):  # Iterate over versions v01 to v04
        date_str = current_date.strftime(date_format)
        file_name = f"{date_str}_EL-CRIDA3_PrelimResults_EN_v{version:02d}.xlsx"  # Format the file name
        file_path = os.path.join(base_directory, file_name)
        file_path = re.sub(r'\\', '/', file_path)
        
        if os.path.exists(file_path):  # Check if the file exists
            df1 = pd.read_excel(file_path, sheet_name='SITE_BZ_NP_PRICES')
            trades = df1.groupby(['DELIVERY_MTU', 'MCP'])['NET_POSITION'].sum().reset_index()
            df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
  
df['DELIVERY_MTU'] = pd.to_datetime(df['DELIVERY_MTU'], format = '%Y-%m-%d %H:%M:%S')
df.info()
result = df.groupby('DELIVERY_MTU').agg({
    'NET_POSITION': 'sum',
    'MCP': 'first'
}).reset_index()     
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\CRIDA 3\CORE 2021.xlsx"
path = path.replace('\\','/')
result.to_excel(path)
############################################################################################################################################################################
"""
XBID
Loop collect the data
ONLY CORE COLLECTION
"""
#2024
#2024
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 CRIDA\XBID"
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 3)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
trades_list = []  # List to store trades DataFrames
while current_date <= end_date:
   
    date_str = current_date.strftime(date_format)
    file_name = f"{date_str}_EL-XBID.xlsx"  # Format the file name
    file_path = os.path.join(base_directory, file_name)
    file_path = re.sub(r'\\', '/', file_path)
        
    if os.path.exists(file_path):  # Check if the file exists
            
        df1 = pd.read_excel(file_path, sheet_name='XBID_Results')
        #df1['WAP'] = df1['VWAP (€/MWh)'] * df1['TOTAL_TRADES']
        trades = df1.groupby(['DELIVERY_DATETIME ', 'VWAP (€/MWh)'])['TOTAL_TRADES'].sum().reset_index()
        df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
df.info()
result = df.groupby('DELIVERY_DATETIME ').agg({
    'TOTAL_TRADES': 'sum',
    'VWAP (€/MWh)': 'first'
}).reset_index()     
    
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\XBID\CORE 2024.xlsx"
path = path.replace('\\','/')
result.to_excel(path,index=False)        
 

#2023
base_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2023 CRIDA\XBID"
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_format = "%Y%m%d"
current_date = start_date


df = pd.DataFrame()
trades_list = []  # List to store trades DataFrames
while current_date <= end_date:
    
    date_str = current_date.strftime(date_format)
    file_name = f"{date_str}_EL-XBID.xlsx"  # Format the file name
    file_path = os.path.join(base_directory, file_name)
    file_path = re.sub(r'\\', '/', file_path)
        
    if os.path.exists(file_path):  # Check if the file exists
            
        df1 = pd.read_excel(file_path, sheet_name='XBID_Results')
            #df1['WAP'] = df1['VWAP (€/MWh)'] * df1['TOTAL_TRADES']
        trades = df1.groupby(['DELIVERY_DATETIME ', 'VWAP (€/MWh)'])['TOTAL_TRADES'].sum().reset_index()
        df = pd.concat([df, trades], axis=0)
    
    current_date += timedelta(days=1)
df.info()
result = df.groupby('DELIVERY_DATETIME ').agg({
    'TOTAL_TRADES': 'sum',
    'VWAP (€/MWh)': 'first'
}).reset_index()     

path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\XBID\CORE 2023.xlsx"
path = path.replace('\\','/')
result.to_excel(path,index=False) 


#########################################################################################################################################################


"""
Sum by month the traded volumes
"""
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Proposal\xbid\creative\DAM.xlsx"
df = pd.read_excel(path, sheet_name='mcp')
df.info()
#df['Total Trades'] = df['NET_POSITION'].abs()
df['Month'] = df['DELIVERY_MTU'].dt.to_period('M')
grouped_df = df.groupby('Month')['MCP'].mean().reset_index()
grouped_df['Average MCP'] = grouped_df['MCP']
grouped_df.head()
grouped_df.to_excel(path, sheet_name = 'Average MCP')
#path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\DAM\CORE 2023.xlsx"
df = pd.read_excel(path, sheet_name='Average MCP')

#df['Total Trades'] = df['NET_POSITION'].abs()
df['Month'] = df['DELIVERY_MTU'].dt.to_period('M')
grouped_df = df.groupby('Month')['TOTAL_TRADES'].sum().reset_index()
grouped_df_mcp = df.groupby('Month')['MCP'].mean().reset_index()
grouped_df['Total Traded GW'] = grouped_df['TOTAL_TRADES']/1000
grouped_df['Total Traded GWh'] = grouped_df['Total Traded GW']/2
grouped_df.set_index('Month', inplace = True)
grouped_df_mcp.set_index('Month', inplace = True)
grouped_df = pd.concat([grouped_df, grouped_df_mcp], axis = 1)
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\Επιφάνεια εργασίας\DAM price prediction\DAM\2023 Volumes.xlsx"
grouped_df.to_excel(path, index = True)
grouped_df.head()
