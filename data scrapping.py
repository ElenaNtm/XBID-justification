# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:31:53 2024

@author: Eleni
Instructions
https://www.enexgroup.gr/documents/20126/353610/YYYYMMDD_EL-CRIDAs_PrelimResults_EN_v%23%23%28Documentation%2C+English+version%29.pdf/0618b46d-6f1e-2a9b-5828-01e992aff409?t=1631791193051
"""

import requests
import json
import os
from datetime import datetime, timedelta

"""
CRIDA 1 
"""
#2023
"""
download_dir = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 CRIDA\CRIDA 1"
download_dir = download_dir.replace('\\','/')

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 7, 14)
date_format = "%Y%m%d"
current_date = start_date

while current_date <= end_date:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Construct the URL for the current date
    current_date_str = current_date.strftime(date_format)
    for version in range(1, 5):  # Iterate over versions v01 to v04
        url = f"https://www.enexgroup.gr/documents/20126/853668/{current_date_str}_EL-CRIDA1_PrelimResults_EN_v{version:02d}.xlsx"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{current_date_str}_EL-CRIDA1.xlsx"
            filepath = os.path.join(download_dir, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download for date {current_date_str}. Status code: {response.status_code}")
        
        # Move to the next date
    current_date += timedelta(days=1)
"""

#2024    

download_dir = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 CRIDA\CRIDA 1"
download_dir = download_dir.replace('\\','/')

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 6, 12)
date_format = "%Y%m%d"
current_date = start_date

while current_date <= end_date:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Construct the URL for the current date
    current_date_str = current_date.strftime(date_format)
    for version in range(1, 5):  # Iterate over versions v01 to v04
        url = f"https://www.enexgroup.gr/documents/20126/853668/{current_date_str}_EL-CRIDA1_PrelimResults_EN_v{version:02d}.xlsx"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{current_date_str}_EL-CRIDA1.xlsx"
            filepath = os.path.join(download_dir, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download for date {current_date_str}. Status code: {response.status_code}")
        
        # Move to the next date
    current_date += timedelta(days=1)

    
"""
CRIDA 2
"""
#2023
"""
download_dir = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\2023 CRIDA\CRIDA 2"
download_dir = download_dir.replace('\\','/')

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_format = "%Y%m%d"
current_date = start_date
print(current_date.strftime(date_format))  # Print the start date in the desired format

while current_date <= end_date:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Construct the URL for the current date
    current_date_str = current_date.strftime(date_format)
    for version in range(1, 5):  # Iterate over versions v01 to v04
        url = f"https://www.enexgroup.gr/documents/20126/853692/{current_date_str}_EL-CRIDA2_PrelimResults_EN_v{version:02d}.xlsx"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{current_date_str}_EL-CRIDA2.xlsx"
            filepath = os.path.join(download_dir, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download for date {current_date_str}. Status code: {response.status_code}")
        
        # Move to the next date
    current_date += timedelta(days=1)    
    
"""

#2024
    
download_dir = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 CRIDA\CRIDA 2"
download_dir = download_dir.replace('\\','/')

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 6, 13)
date_format = "%Y%m%d"
current_date = start_date
print(current_date.strftime(date_format))  # Print the start date in the desired format

while current_date <= end_date:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Construct the URL for the current date
    current_date_str = current_date.strftime(date_format)
    for version in range(1, 5):  # Iterate over versions v01 to v04
        url = f"https://www.enexgroup.gr/documents/20126/853692/{current_date_str}_EL-CRIDA2_PrelimResults_EN_v{version:02d}.xlsx"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{current_date_str}_EL-CRIDA2.xlsx"
            filepath = os.path.join(download_dir, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download for date {current_date_str}. Status code: {response.status_code}")
        
        # Move to the next date
    current_date += timedelta(days=1)    
   
"""
CRIDA 3
"""
#2023
"""
download_dir = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\2023 CRIDA\CRIDA 3"
download_dir = download_dir.replace('\\','/')

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_format = "%Y%m%d"
current_date = start_date
print(current_date.strftime(date_format))  # Print the start date in the desired format

while current_date <= end_date:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Construct the URL for the current date
    current_date_str = current_date.strftime(date_format)
    for version in range(1, 5):  # Iterate over versions v01 to v04
        url = f"https://www.enexgroup.gr/documents/20126/855431/{current_date_str}_EL-CRIDA3_PrelimResults_EN_v{version:02d}.xlsx"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{current_date_str}_EL-CRIDA3.xlsx"
            filepath = os.path.join(download_dir, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download for date {current_date_str}. Status code: {response.status_code}")
        
        # Move to the next date
    current_date += timedelta(days=1)    
    
"""

#2024
    
download_dir = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 CRIDA\CRIDA 3"
download_dir = download_dir.replace('\\','/')

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 6, 13)
date_format = "%Y%m%d"
current_date = start_date
print(current_date.strftime(date_format))  # Print the start date in the desired format

while current_date <= end_date:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Construct the URL for the current date
    current_date_str = current_date.strftime(date_format)
    for version in range(1, 5):  # Iterate over versions v01 to v04
        url = f"https://www.enexgroup.gr/documents/20126/855431/{current_date_str}_EL-CRIDA3_PrelimResults_EN_v{version:02d}.xlsx"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{current_date_str}_EL-CRIDA3.xlsx"
            filepath = os.path.join(download_dir, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download for date {current_date_str}. Status code: {response.status_code}")
        
        # Move to the next date
    current_date += timedelta(days=1) 
    
    
"""
XBID 

"""
#2023
"""
download_dir = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\2023 CRIDA\XBID"
download_dir = download_dir.replace('\\','/')

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_format = "%Y%m%d"
current_date = start_date
print(current_date.strftime(date_format))  # Print the start date in the desired format

while current_date <= end_date:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Construct the URL for the current date
    current_date_str = current_date.strftime(date_format)
    for version in range(1, 5):  # Iterate over versions v01 to v04
        url = f"https://www.enexgroup.gr/documents/20126/1550281/{current_date_str}_EL-XBID_Results_EN_v{version:02d}.xlsx"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{current_date_str}_EL-XBID.xlsx"
            filepath = os.path.join(download_dir, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download for date {current_date_str}. Status code: {response.status_code}")
        
        # Move to the next date
    current_date += timedelta(days=1)    
    
"""
#2024
   
download_dir = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 CRIDA\XBID"
download_dir = download_dir.replace('\\','/')

start_date = datetime(2024, 6, 14)
end_date = datetime(2024, 7, 10)
date_format = "%Y%m%d"
current_date = start_date
print(current_date.strftime(date_format))  # Print the start date in the desired format

while current_date <= end_date:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Construct the URL for the current date
    current_date_str = current_date.strftime(date_format)
    for version in range(1, 5):  # Iterate over versions v01 to v04
        url = f"https://www.enexgroup.gr/documents/20126/1550281/{current_date_str}_EL-XBID_Results_EN_v{version:02d}.xlsx"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{current_date_str}_EL-XBID.xlsx"
            filepath = os.path.join(download_dir, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download for date {current_date_str}. Status code: {response.status_code}")
        
        # Move to the next date
    current_date += timedelta(days=1) 
    
    
"""
DAM 2024
"""
download_dir = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 DAM"
download_dir = download_dir.replace('\\','/')

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 7, 10)
date_format = "%Y%m%d"
current_date = start_date
print(current_date.strftime(date_format))  # Print the start date in the desired format

while current_date <= end_date:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Construct the URL for the current date
    current_date_str = current_date.strftime(date_format)
    for version in range(1, 5):  # Iterate over versions v01 to v04
        url = f"https://www.enexgroup.gr/documents/20126/200106/{current_date_str}_EL-DAM_Results_EN_v{version:02d}.xlsx"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{current_date_str}_EL-DAM_PrelimResults_EN_v01.xls"
            filepath = os.path.join(download_dir, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download for date {current_date_str}. Status code: {response.status_code}")
        
        # Move to the next date
    current_date += timedelta(days=1)     
"""
IDA1
"""
download_dir = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 CRIDA\IDA 1"
download_dir = download_dir.replace('\\','/')



start_date = datetime(2024, 6, 14)
end_date = datetime(2024, 7, 10)
date_format = "%Y%m%d"
current_date = start_date
print(current_date.strftime(date_format))  # Print the start date in the desired format

while current_date <= end_date:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Construct the URL for the current date
    current_date_str = current_date.strftime(date_format)
    for version in range(1, 5):  # Iterate over versions v01 to v04
        url = f"https://www.enexgroup.gr/documents/20126/3257249/{current_date_str}_EL-IDA1_Results_EN_v{version:02d}.xlsx"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{current_date_str}_EL-IDA1.xlsx"
            filepath = os.path.join(download_dir, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download for date {current_date_str}. Status code: {response.status_code}")
        
        # Move to the next date
    current_date += timedelta(days=1)  
"""
IDA2
"""
download_dir = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 CRIDA\IDA 2"
download_dir = download_dir.replace('\\','/')



start_date = datetime(2024, 6, 14)
end_date = datetime(2024, 7, 10)
date_format = "%Y%m%d"
current_date = start_date
print(current_date.strftime(date_format))  # Print the start date in the desired format

while current_date <= end_date:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Construct the URL for the current date
    current_date_str = current_date.strftime(date_format)
    for version in range(1, 5):  # Iterate over versions v01 to v04
        url = f"https://www.enexgroup.gr/documents/20126/3257281/{current_date_str}_EL-IDA2_Results_EN_v{version:02d}.xlsx"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{current_date_str}_EL-IDA2.xlsx"
            filepath = os.path.join(download_dir, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download for date {current_date_str}. Status code: {response.status_code}")
        
        # Move to the next date
    current_date += timedelta(days=1)  
    
"""
IDA3
"""
download_dir = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 CRIDA\IDA 3"
download_dir = download_dir.replace('\\','/')



start_date = datetime(2024, 6, 14)
end_date = datetime(2024, 7, 10)
date_format = "%Y%m%d"
current_date = start_date
print(current_date.strftime(date_format))  # Print the start date in the desired format

while current_date <= end_date:
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Construct the URL for the current date
    current_date_str = current_date.strftime(date_format)
    for version in range(1, 5):  # Iterate over versions v01 to v04
        url = f"https://www.enexgroup.gr/documents/20126/3257522/{current_date_str}_EL-IDA3_Results_EN_v{version:02d}.xlsx"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{current_date_str}_EL-IDA3.xlsx"
            filepath = os.path.join(download_dir, filename)
            
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download for date {current_date_str}. Status code: {response.status_code}")
        
        # Move to the next date
    current_date += timedelta(days=1)     